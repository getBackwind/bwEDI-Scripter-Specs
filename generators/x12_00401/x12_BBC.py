# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BBC(Segment):
    """
    BBC - Legal Claims
    
    Description:
        To identify the basis and type of a legal claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BBC/
    """
    _id: Literal["BBC"] = id_element(name="BBC")

    ClaimTypeCode: X12ID = element(
        name="BBC01",
        description="Claim Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="BBC02",
        description="Description",
        min_length=1,
        max_length=80,
    )
