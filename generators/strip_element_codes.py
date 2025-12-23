import json
import sys
from typing import Any, Dict


def strip_codes(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove 'codes' from every element in every segment.
    """
    segments = data.get("segments", [])
    for seg in segments:
        for el in seg.get("elements", []):
            if "codes" in el:
                el.pop("codes", None)
    return data


def main():
    if len(sys.argv) != 3:
        print("Usage: python strip_element_codes.py <input.json> <output.json>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data = strip_codes(data)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✔ Wrote code-free JSON to {output_path}")


if __name__ == "__main__":
    main()
