# bwEDI-Scripter-Specs

Public EDI Segment Specification Repository

## Overview

This repository provides structured, versioned **EDI segment definitions** and a minimal core API reference for building **Python-based EDI transaction definitions and mapping scripts**.

It is designed for use by automated tools such as **EDI Scripter**, which generate:

- `definition.py` — transaction and loop definitions  
- `mapper.py` — mapping logic from structured models (e.g. Pydantic) to EDI  

from client implementation guides and structured data models.

---

## Repository Layout

```
bwEDI-Scripter-Specs/
│
├── examples/
│   ├── 810_example.py
│   ├── 850_example.py
│   └── 855_example.py
│
├── x12_00401/
│   ├── x12_AAA.py
│   ├── x12_NM1.py
│   └── ...
│
├── x12_00501/
│   ├── x12_AAA.py
│   └── ...
│
├── core_classes_min.py
├── x12_00401_index.json
├── x12_00501_index.json
└── README.md
```

---

## Segment Definitions

Each file under `x12_00401/` or `x12_00501/` defines **one X12 segment** using the EDI DSL.

```python
class AAA(Segment):
    """AAA - Request Validation"""
    _id: Literal["AAA"] = id_element(name="AAA")

    YesNoConditionOrResponseCode: X12ID = element(
        name="AAA01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
```

These files are the **canonical source of truth** for all X12 segment structures.

---

## Core API (`core_classes_min.py`)

A minimal, dependency-light subset of the internal EDI framework, including:

- `Segment`
- `element()`, `id_element()`
- Common X12 data types (`X12ID`, `X12AN`, `X12DT`, etc.)
- `DocumentConfiguration` (delimiter control)
- `EdiFlatHeader` (ISA / GS / ST metadata)

This allows external generators to reproduce the DSL syntax **without importing the full internal package**.

---

## Index Files

Index files map **segment IDs → raw GitHub URLs**.

Example: `x12_00401_index.json`

```json
{
  "AAA": "https://raw.githubusercontent.com/getBackwind/bwEDI-Scripter-Specs/main/x12_00401/x12_AAA.py",
  "NM1": "https://raw.githubusercontent.com/getBackwind/bwEDI-Scripter-Specs/main/x12_00401/x12_NM1.py"
}
```

These enable **on-demand fetching** of only the segments required by a transaction.

---

## Examples

The `examples/` directory shows real-world usage patterns:

Each example includes:
- Transaction and loop definitions
- Mapping functions from a Pydantic-style model
- Optional serialization/testing snippets

Example (`850_example.py`):

```python
from x12_00401.x12_N1 import N1
from core_classes_min import Segment

class PO1Loop(Segment):
    _id = "PO1"

def map_order_to_edi(order):
    return PO1Loop(
        ProductID=order.sku,
        Quantity=order.quantity,
    )
```

---

## How EDI Scripter Uses This Repo

1. Detect X12 version from client spec (e.g. `004010`)
2. Load the corresponding index JSON
3. Fetch required segment definitions dynamically
4. Parse the implementation guide for loop/segment order
5. Generate:
   - `definition.py`
   - `mapper.py`
6. Reference `core_classes_min.py` for DSL structure and types

---

## Consuming This Repo Programmatically

### Dynamic Fetch Example

```python
import requests

url = "https://raw.githubusercontent.com/getBackwind/bwEDI-Scripter-Specs/main/x12_00401/x12_AAA.py"
code = requests.get(url).text
exec(code, globals())

print(AAA)
```

### Tool-Based Consumption

- Load `x12_00401_index.json`
- Fetch only referenced segments
- Assemble transaction definitions
- Generate mappers using examples as style guidance

---

## Raw URL Patterns

| Version | Segment | URL |
|-------|--------|-----|
| 004010 | AAA | https://raw.githubusercontent.com/getBackwind/bwEDI-Scripter-Specs/main/x12_00401/x12_AAA.py |
| 004010 | NM1 | https://raw.githubusercontent.com/getBackwind/bwEDI-Scripter-Specs/main/x12_00401/x12_NM1.py |
| 005010 | AAA | https://raw.githubusercontent.com/getBackwind/bwEDI-Scripter-Specs/main/x12_00501/x12_AAA.py |

---

## Optional Tooling

You may include utilities under `/tools`:

- `build_index.py` — regenerate index JSONs
- `validate_segments.py` — validate element definitions
- `export_segments_to_json.py` — produce language-neutral exports

---

## Summary

| Component | Purpose |
|---------|--------|
| `x12_00401/`, `x12_00501/` | Authoritative segment definitions |
| `core_classes_min.py` | Minimal DSL & types |
| `examples/` | Transaction & mapper patterns |
| `x12_####_index.json` | Fast segment lookup |
| EDI Scripter | Auto-generates transactions & mappers |
