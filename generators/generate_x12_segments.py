#!/usr/bin/env python3
"""
generate_x12_segments_v3.py

Takes a "nocodes" JSON (output of strip_codes.py) and generates a Python package
of segment class definitions.

Grouping:
- If --grouped true (default): group alphabetically into files: x12_a.py, x12_b.py, ...
- If --grouped false: put each segment in its own file: <SEG>.py (e.g., BIG.py)

Backwards compatibility:
- If a segment/element already exists in the legacy definitions.py AND it was defined
  using element(...), keep the *attribute name* (field name).
- If a legacy field was defined as null_element(...), DO NOT preserve its attribute
  name; generate a new semantic attribute name instead.

This generator NEVER emits null_element() fields.

Class docstrings:
- Adds segment name, description, and source URL (if present in JSON) to the class docstring.

Typing:
- Uses X12 datatypes from x12_types.py (X12AN, X12ID, X12DT, X12TM, X12R, X12N0..X12N9, X12B, X12Z, X12Nn).
- Mandatory (requirement == "M") -> non-Optional type
- Optional -> Optional[type]
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

X12_TYPE_MAP: Dict[str, str] = {
    "AN": "X12AN",
    "ID": "X12ID",
    "Z": "X12Z",
    "DT": "X12DT",
    "TM": "X12TM",
    "R": "X12R",
    "B": "X12B",
    "N": "X12Nn",
    **{f"N{i}": f"X12N{i}" for i in range(10)},
}

def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()

def get_call_name(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Call):
        fn = node.func
        if isinstance(fn, ast.Name):
            return fn.id
        if isinstance(fn, ast.Attribute):
            return fn.attr
    return None

def get_kw_str(call: ast.Call, key: str) -> Optional[str]:
    for kw in call.keywords:
        if kw.arg == key and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
            return kw.value.value
    return None

def parse_legacy_definitions(path: str) -> Dict[str, Dict[str, Tuple[str, str]]]:
    """Return {SEG: {POS: (attr_name, kind)}} where kind is element/null_element."""
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    mod = ast.parse(src)
    seg_map: Dict[str, Dict[str, Tuple[str, str]]] = {}

    for node in mod.body:
        if not isinstance(node, ast.ClassDef):
            continue
        is_segment = any(
            (isinstance(b, ast.Name) and b.id == "Segment") or (isinstance(b, ast.Attribute) and b.attr == "Segment")
            for b in node.bases
        )
        if not is_segment:
            continue

        seg_id = node.name
        elem_map: Dict[str, Tuple[str, str]] = {}

        for stmt in node.body:
            if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name) and isinstance(stmt.value, ast.Call):
                attr = stmt.target.id
                cname = get_call_name(stmt.value)
                if cname in {"element", "null_element"}:
                    title = get_kw_str(stmt.value, "name")
                    if title:
                        elem_map[title] = (attr, cname)

        if elem_map:
            seg_map[seg_id] = elem_map

    return seg_map

def to_identifier(desc: str) -> str:
    desc = normalize_ws(desc or "")
    if not desc:
        return ""
    desc = re.sub(r"[^A-Za-z0-9 ]+", " ", desc)
    parts = [p for p in re.split(r"\s+", desc) if p]
    if not parts:
        return ""
    ident = "".join(p[:1].upper() + p[1:] for p in parts)
    if ident and ident[0].isdigit():
        ident = "E" + ident
    if ident in {"Class", "From", "Import", "None", "True", "False"}:
        ident += "Value"
    return ident

def safe_attr(existing: set[str], cand: str, fallback: str) -> str:
    if not cand or not re.match(r"^[A-Za-z_]\w*$", cand):
        cand = fallback
    if cand not in existing:
        existing.add(cand)
        return cand
    i = 2
    while f"{cand}{i}" in existing:
        i += 1
    cand2 = f"{cand}{i}"
    existing.add(cand2)
    return cand2

def ann_type(dt: Optional[str], mandatory: bool) -> Tuple[str, str]:
    t = X12_TYPE_MAP.get(dt or "", "str")
    if mandatory:
        return t, t
    return f"Optional[{t}]", t

def write_file(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

def parse_bool(s: str) -> bool:
    return str(s).strip().lower() in {"1", "true", "t", "yes", "y", "on"}

def build_class_block(seg: Dict[str, Any], legacy: Dict[str, Dict[str, Tuple[str, str]]], needed_types: set[str]) -> str:
    seg_id = seg["segment_id"]
    elements = seg.get("elements") or []
    legacy_seg = legacy.get(seg_id, {})

    existing_names: set[str] = set()
    for (_pos, (attr, kind)) in legacy_seg.items():
        if kind == "element":
            existing_names.add(attr)

    seg_name = seg.get("name") or seg_id
    seg_desc = seg.get("description")
    seg_url = seg.get("url")

    doc_lines = [f"{seg_id} - {seg_name}"]
    if seg_desc:
        doc_lines += ["", "Description:", f"    {normalize_ws(str(seg_desc))}"]
    if seg_url:
        doc_lines += ["", "Source:", f"    {str(seg_url).strip()}"]

    docstring = '    """\n' + "\n".join(f"    {line}" for line in doc_lines) + '\n    """'

    cls_lines: List[str] = [
        f"class {seg_id}(Segment):",
        docstring,
        f'    _id: Literal["{seg_id}"] = id_element(name="{seg_id}")',
        "",
    ]

    for el in elements:
        pos = el.get("position") or el.get("name")
        if not pos:
            continue

        mandatory = (el.get("requirement") == "M")

        min_len = el.get("min_length")
        max_len = el.get("max_length")
        try:
            min_len = int(min_len) if min_len is not None else None
        except Exception:
            min_len = None
        try:
            max_len = int(max_len) if max_len is not None else None
        except Exception:
            max_len = None

        desc = el.get("description")
        desc = normalize_ws(desc) if isinstance(desc, str) else None

        if pos in legacy_seg and legacy_seg[pos][1] == "element":
            attr_name = legacy_seg[pos][0]
        else:
            cand = to_identifier(el.get("name") or desc or "")
            attr_name = safe_attr(existing_names, cand, pos)

        dt = el.get("data_type")
        ann, used = ann_type(dt, mandatory)
        if used.startswith("X12"):
            needed_types.add(used)

        d = el.get("name") or desc or pos
        d = normalize_ws(str(d))

        cls_lines.append(f"    {attr_name}: {ann} = element(")
        cls_lines.append(f"        name=\"{pos}\",")
        cls_lines.append(f"        description={json.dumps(d)},")
        if mandatory:
            cls_lines.append("        mandatory=True,")
        if min_len is not None:
            cls_lines.append(f"        min_length={min_len},")
        if max_len is not None:
            cls_lines.append(f"        max_length={max_len},")
        cls_lines.append("    )")
        cls_lines.append("")

    return "\n".join(cls_lines).rstrip() + "\n"

def build_module(module_path: str, class_blocks: List[str], needed_types: set[str]) -> None:
    imports = [
        "# Auto-generated. Do not edit by hand.",
        "from __future__ import annotations",
        "",
        "from typing import Optional, Literal",
        "from bwEDI.segment import Segment, element, id_element",
    ]
    if needed_types:
        imports.append("from bwEDI.x12_types import " + ", ".join(sorted(needed_types)))
    imports.append("")
    content = "\n".join(imports) + "\n\n" + "\n\n".join(class_blocks).rstrip() + "\n"
    write_file(module_path, content)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True, help="Input nocodes JSON")
    ap.add_argument("--definitions", required=True, help="Path to legacy definitions.py (for preserving names)")
    ap.add_argument("--out", required=True, help="Output directory for generated package")
    ap.add_argument("--base-url", default="", help="Base URL prefix for index JSON values (e.g. https://raw.githubusercontent.com/your-org/x12-definitions/main/x12_00401/)")
    ap.add_argument("--index-name", default="index.json", help="Filename for generated index JSON")
    ap.add_argument("--grouped", default="true", help="true: group alphabetically. false: one segment per file")
    args = ap.parse_args()

    grouped_mode = parse_bool(args.grouped)

    with open(args.json, "r", encoding="utf-8") as f:
        data = json.load(f)

    segments: List[Dict[str, Any]] = data.get("segments", [])
    legacy = parse_legacy_definitions(args.definitions)

    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    init_lines = [
        "# Auto-generated. Do not edit by hand.",
        "",
    ]

    if grouped_mode:
        grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for seg in segments:
            seg_id = seg.get("segment_id") or ""
            if not seg_id:
                continue
            letter = seg_id[0].lower()
            if not ("a" <= letter <= "z"):
                letter = "other"
            grouped[letter].append(seg)

        for letter in sorted(grouped.keys()):
            mod_name = f"x12_{letter}"
            segs = sorted(grouped[letter], key=lambda s: s.get("segment_id", ""))

            needed_types: set[str] = set()
            class_blocks: List[str] = []
            for seg in segs:
                if seg.get("segment_id"):
                    class_blocks.append(build_class_block(seg, legacy, needed_types))

            build_module(os.path.join(out_dir, f"{mod_name}.py"), class_blocks, needed_types)
            init_lines.append(f"from .{mod_name} import *  # noqa: F401,F403")

    else:
        for seg in sorted(segments, key=lambda s: s.get("segment_id", "")):
            seg_id = seg.get("segment_id") or ""
            if not seg_id:
                continue
            mod_name = seg_id
            needed_types: set[str] = set()
            class_blocks = [build_class_block(seg, legacy, needed_types)]
            build_module(os.path.join(out_dir, f"x12_{mod_name}.py"), class_blocks, needed_types)
            init_lines.append(f"from .x12_{mod_name} import {seg_id}  # noqa: F401")

    init_lines.append("")
    # Build index JSON mapping SEG -> URL to the module file (or grouped module)
    # The URL is base-url + filename. If base-url is empty, store relative filename only.
    index: Dict[str, str] = {}

    def _join_url(base_url: str, filename: str) -> str:
        base_url = (base_url or "").strip()
        if not base_url:
            return filename
        if not base_url.endswith("/"):
            base_url += "/"
        return base_url + filename

    if grouped_mode:
        # Map each segment to its grouped module file name (x12_a.py etc)
        grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for seg in segments:
            seg_id = seg.get("segment_id") or ""
            if not seg_id:
                continue
            letter = seg_id[0].lower()
            if not ("a" <= letter <= "z"):
                letter = "other"
            grouped[letter].append(seg)

        for letter, segs in grouped.items():
            filename = f"x12_{letter}.py"
            for seg in segs:
                seg_id = seg.get("segment_id") or ""
                if seg_id:
                    index[seg_id] = _join_url(args.base_url, filename)
    else:
        for seg in segments:
            seg_id = seg.get("segment_id") or ""
            if seg_id:
                index[seg_id] = _join_url(args.base_url, f"x12_{seg_id}.py")

    # Write index json
    index_path = os.path.join(out_dir, args.index_name)
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(dict(sorted(index.items())), f, ensure_ascii=False, indent=2)

    write_file(os.path.join(out_dir, "__init__.py"), "\n".join(init_lines))

    print(f"Generated package at: {out_dir}")
    print(f"Grouping mode: {'alphabetical' if grouped_mode else 'per-segment'}")

if __name__ == "__main__":
    main()
