# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LQ(Segment):
    """
    LQ - Industry Code
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LQ/
    """
    _id: Literal["LQ"] = id_element(name="LQ")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="LQ01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="LQ02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
