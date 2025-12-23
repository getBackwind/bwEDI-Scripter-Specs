#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import time
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; X12SegmentScraper/1.0; +https://example.com)"
}

SEGMENT_HREF_RE = re.compile(r"/schema/edi/x12/\d{5}/segments/[A-Z0-9]{2,3}/?$")
ELEMENT_CODE_RE = re.compile(r"^[A-Z0-9]{2,4}\d{2}$")  # AAA01 etc.
NUMERIC_RE = re.compile(r"^\d+$")


@dataclass
class CodeItem:
    code: str
    meaning: str


@dataclass
class ElementSpec:
    position: str          # e.g. AAA01
    element_id: str        # e.g. 1073
    name: str              # e.g. Yes/No Condition or Response Code
    data_type: Optional[str] = None  # ID / AN / DT / Nn etc.
    requirement: Optional[str] = None  # M / O (site shows Chinese too)
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    description: Optional[str] = None
    codes: Optional[List[CodeItem]] = None


@dataclass
class SegmentSpec:
    segment_id: str        # e.g. AAA
    name: str              # e.g. Request Validation
    description: Optional[str]
    url: str
    elements: List[ElementSpec]


def fetch(session: requests.Session, url: str, timeout: int = 30, retries: int = 4, backoff: float = 1.6) -> str:
    last_err = None
    for attempt in range(retries):
        try:
            r = session.get(url, timeout=timeout, headers=DEFAULT_HEADERS)
            r.raise_for_status()
            return r.text
        except Exception as e:
            last_err = e
            sleep_s = (backoff ** attempt)
            time.sleep(sleep_s)
    raise RuntimeError(f"Failed to fetch {url}: {last_err}")


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def get_release_segment_links(index_html: str, base_url: str) -> List[str]:
    """
    Extract only the segment links from the release page.
    The page contains many transaction-set links too; we filter to /segments/XXX/.
    """
    soup = BeautifulSoup(index_html, "lxml")

    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        abs_url = urljoin(base_url, href)

        # Normalize trailing slash (both exist)
        if abs_url.endswith("/"):
            abs_url_norm = abs_url[:-1]
        else:
            abs_url_norm = abs_url

        if SEGMENT_HREF_RE.search(abs_url_norm):
            links.append(abs_url_norm + "/")  # keep consistent with trailing slash

    # Deduplicate while preserving order
    seen = set()
    out = []
    for u in links:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def extract_segment_header(soup: BeautifulSoup) -> Tuple[str, str, Optional[str]]:
    """
    Returns (segment_id, name, description).
    On the site, the segment header appears like:
      AAA  Request Validation
      <description sentence...>
    """
    # Try to find the breadcrumb / title area: often includes the segment code as its own nav item.
    text = soup.get_text("\n", strip=True)

    # Segment ID: prefer breadcrumb last token or the first standalone 2-3 char uppercase token near top.
    # Safer: look for a link whose href ends with /segments/XXX/
    seg_id = None
    for a in soup.find_all("a", href=True):
        href = a["href"]
        m = re.search(r"/segments/([A-Z0-9]{2,3})/?$", href)
        if m:
            seg_id = m.group(1)
            break

    if not seg_id:
        # Fallback: scan visible text lines
        for line in soup.get_text("\n", strip=True).split("\n")[:40]:
            if re.fullmatch(r"[A-Z0-9]{2,3}", line.strip()):
                seg_id = line.strip()
                break

    if not seg_id:
        raise ValueError("Could not determine segment_id")

    # Name: find occurrences like "AAA" + next heading-ish text
    # Usually there are two adjacent links: AAA and "Request Validation"
    seg_name = None
    candidates = []
    for a in soup.find_all("a"):
        t = normalize_ws(a.get_text(" ", strip=True))
        if t == seg_id:
            # Look forward to the next <a> text
            nxt = a.find_next("a")
            if nxt:
                nt = normalize_ws(nxt.get_text(" ", strip=True))
                if nt and nt != seg_id:
                    candidates.append(nt)
    if candidates:
        seg_name = candidates[0]

    if not seg_name:
        # Fallback: title tag
        if soup.title and soup.title.string:
            # e.g. "EDI X12 00401 AAA Segment Schema | ..."
            m = re.search(rf"\b{re.escape(seg_id)}\b\s+(.+?)\s+Segment\b", soup.title.string)
            if m:
                seg_name = normalize_ws(m.group(1))

    if not seg_name:
        seg_name = ""

    # Description: usually the first paragraph-ish sentence under the header
    # We take the first non-empty line after the "To " line marker if present, else best effort.
    desc = None
    lines = soup.get_text("\n", strip=True).split("\n")
    # Find the line that equals the segment name and take the next informative line.
    for i, line in enumerate(lines):
        if normalize_ws(line) == seg_name and i + 1 < len(lines):
            possible = normalize_ws(lines[i + 1])
            # Often description starts with "To ..."
            if possible and possible.lower().startswith("to "):
                desc = possible
                break
    if not desc:
        for line in lines:
            l = normalize_ws(line)
            if l.lower().startswith("to ") and len(l) > 10:
                desc = l
                break

    return seg_id, seg_name, desc


def parse_codes_block(li: Any) -> Optional[List[CodeItem]]:
    """
    In the site text, codes appear as:
      Codes (N)
        * X Meaning
        * Y Meaning
    This is usually a <ul> nested under something.
    We'll search within the element block for list items that look like "CODE Meaning".
    """
    # Search nearby for "Codes" label
    container_text = li.get_text("\n", strip=True)
    if "Codes" not in container_text:
        return None

    codes: List[CodeItem] = []
    # Search all list items within the same element section
    for sub_li in li.find_all("li"):
        t = normalize_ws(sub_li.get_text(" ", strip=True))
        # Match "N No" or "10 Alabama"
        parts = t.split(" ", 1)
        if len(parts) != 2:
            continue
        code, meaning = parts[0].strip(), parts[1].strip()
        if not code or not meaning:
            continue
        # Codes can be alpha (N) or numeric (10) etc.
        if re.fullmatch(r"[A-Z0-9]{1,3}", code) or re.fullmatch(r"\d{1,3}", code):
            codes.append(CodeItem(code=code, meaning=meaning))

    return codes or None


def parse_elements(soup: BeautifulSoup) -> List[ElementSpec]:
    """
    Robustly locate the elements <ul> by scanning all ULs and picking the one
    that actually contains element position codes like AAA01, AD101, etc.

    Then parse each element LI by using tokenized DOM text (li.stripped_strings).
    Also extracts Min/Max lengths when present (e.g. "Min 2 / Max 2").
    """
    # --- 1) Find the UL that contains the element list (AAA01-like anchors) ---
    candidate_uls: List[Tuple[int, Any]] = []
    for ul in soup.find_all("ul"):
        anchors = ul.find_all("a")
        if not anchors:
            continue

        count_positions = 0
        for a in anchors:
            t = normalize_ws(a.get_text(" ", strip=True))
            if ELEMENT_CODE_RE.fullmatch(t):
                count_positions += 1

        if count_positions > 0:
            candidate_uls.append((count_positions, ul))

    if not candidate_uls:
        return []

    candidate_uls.sort(key=lambda x: x[0], reverse=True)
    ul = candidate_uls[0][1]

    out: List[ElementSpec] = []

    dtype_re = re.compile(r"^[A-Z]{1,3}\d?$")  # ID, AN, DT, TM, N2, R, etc.
    req_re = re.compile(r"^(M|O)\b")           # Mandatory / Optional marker
    minmax_re = re.compile(r"^Min\s+(\d+)\s*/\s*Max\s+(\d+)\s*$", re.IGNORECASE)

    # If the site shows multilingual requirement text, it often contains these:
    mandatory_noise_re = re.compile(r"(Mandatory|Optional|必须|可选)", re.IGNORECASE)

    def _clean_tokens(li_tag: Any) -> List[str]:
        toks: List[str] = []
        for s in li_tag.stripped_strings:
            t = normalize_ws(str(s))
            if t:
                toks.append(t)
        return toks

    def _looks_like_description(t: str) -> bool:
        tl = t.lower()
        if not t or len(t) < 8:
            return False
        if tl.startswith("codes"):
            return False
        if minmax_re.match(t):
            return False
        if mandatory_noise_re.search(t):
            return False
        if tl in {"code", "codes", "elements", "element"}:
            return False
        # Descriptions often begin with these patterns
        if tl.startswith("to ") or tl.startswith("code ") or tl.startswith("the ") or tl.startswith("a "):
            return True
        return True

    for li in ul.find_all("li", recursive=True):
        anchors = li.find_all("a")
        if len(anchors) < 2:
            continue

        pos = normalize_ws(anchors[0].get_text(" ", strip=True))
        elid = normalize_ws(anchors[1].get_text(" ", strip=True))
        if not (ELEMENT_CODE_RE.fullmatch(pos) and NUMERIC_RE.fullmatch(elid)):
            continue

        tokens = _clean_tokens(li)

        # tokens typically: [ADV02, 1000, Service Characteristics Qualifier, AN, M 必须(Mandatory), Min 2 / Max 2, Code from..., Codes(...), ...]
        try:
            i_pos = tokens.index(pos)
        except ValueError:
            i_pos = 0

        try:
            i_elid = tokens.index(elid, i_pos + 1)
        except ValueError:
            continue

        name = tokens[i_elid + 1] if (i_elid + 1) < len(tokens) else ""
        if not name:
            continue

        tail = tokens[i_elid + 2 :]

        data_type: Optional[str] = None
        requirement: Optional[str] = None
        min_length: Optional[int] = None
        max_length: Optional[int] = None
        desc: Optional[str] = None

        # datatype
        for t in tail:
            if dtype_re.fullmatch(t):
                data_type = t
                break

        # requirement marker (M/O) - token may be "M 必须(Mandatory)"
        for t in tail:
            mreq = req_re.match(t)
            if mreq:
                requirement = mreq.group(1)
                break

        # min/max length
        for t in tail:
            mm = minmax_re.match(t)
            if mm:
                try:
                    min_length = int(mm.group(1))
                    max_length = int(mm.group(2))
                except ValueError:
                    pass
                break

        # description: first real description token after skipping datatype/req/minmax and stopping at Codes
        for t in tail:
            if dtype_re.fullmatch(t):
                continue
            if req_re.match(t):
                continue
            if minmax_re.match(t):
                continue
            if t.lower().startswith("codes"):
                break
            if _looks_like_description(t):
                desc = t
                break

        codes = parse_codes_block(li)

        # If the page didn't provide Min/Max explicitly, infer from codes list
        if (min_length is None or max_length is None) and codes:
            cmin, cmax = _infer_minmax_from_codes(codes)
            if min_length is None:
                min_length = cmin
            if max_length is None:
                max_length = cmax


        out.append(
            ElementSpec(
                position=pos,
                element_id=elid,
                name=name,
                data_type=data_type,
                requirement=requirement,
                min_length=min_length,
                max_length=max_length,
                description=desc,
                codes=codes,
            )
        )

    return out


def _infer_minmax_from_codes(codes: Optional[List[CodeItem]]) -> Tuple[Optional[int], Optional[int]]:
    if not codes:
        return None, None
    lengths = [len((c.code or "").strip()) for c in codes]
    lengths = [n for n in lengths if n > 0]
    if not lengths:
        return None, None
    return min(lengths), max(lengths)


def parse_segment_page(html: str, url: str) -> SegmentSpec:
    soup = BeautifulSoup(html, "lxml")
    seg_id, seg_name, seg_desc = extract_segment_header(soup)
    elements = parse_elements(soup)
    return SegmentSpec(
        segment_id=seg_id,
        name=seg_name,
        description=seg_desc,
        url=url,
        elements=elements,
    )


def load_existing(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return {}


def main() -> None:
    ap = argparse.ArgumentParser(description="Scrape X12 segment specs from kasoftware.com into JSON.")
    ap.add_argument("--index-url", required=True, help="Release index URL, e.g. https://www.kasoftware.com/schema/edi/x12/00401/")
    ap.add_argument("--out", default="x12_segments.json", help="Output JSON file path.")
    ap.add_argument("--delay", type=float, default=0.25, help="Delay between requests in seconds.")
    ap.add_argument("--max", type=int, default=0, help="Max number of segments to scrape (0 = all).")
    ap.add_argument("--resume", action="store_true", help="Resume by skipping segments already in output JSON.")
    args = ap.parse_args()

    base_url = args.index_url if args.index_url.endswith("/") else args.index_url + "/"

    session = requests.Session()

    index_html = fetch(session, base_url)
    segment_urls = get_release_segment_links(index_html, base_url)

    if args.max and args.max > 0:
        segment_urls = segment_urls[: args.max]

    existing = load_existing(args.out) if args.resume else {}
    existing_segments: Dict[str, Any] = {}
    if isinstance(existing, dict) and "segments" in existing and isinstance(existing["segments"], list):
        for seg in existing["segments"]:
            if isinstance(seg, dict) and "segment_id" in seg:
                existing_segments[str(seg["segment_id"])] = seg

    results: List[Dict[str, Any]] = []
    # Keep existing ones first if resuming
    if existing_segments:
        results.extend(existing_segments.values())

    already = set(existing_segments.keys())

    for seg_url in tqdm(segment_urls, desc="Scraping segments"):
        seg_code = seg_url.rstrip("/").split("/")[-1]
        if args.resume and seg_code in already:
            continue

        html = fetch(session, seg_url)
        spec = parse_segment_page(html, seg_url)
        results.append(asdict(spec))

        # polite throttling
        time.sleep(args.delay)

        # incremental write so you can stop anytime
        payload = {
            "source": base_url,
            "segment_count": len(results),
            "segments": results,
        }
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Done. Wrote {len(results)} segments to {args.out}")


if __name__ == "__main__":
    main()
