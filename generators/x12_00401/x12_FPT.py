# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class FPT(Segment):
    """
    FPT - Financial Participation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FPT/
    """
    _id: Literal["FPT"] = id_element(name="FPT")

    TypeOfAccountCode: X12ID = element(
        name="FPT01",
        description="Type of Account Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="FPT02",
        description="Percent",
        min_length=1,
        max_length=10,
    )
