# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G2(Segment):
    """
    G2 - Beyond Routing
    
    Description:
        To specify routing of a beyond point
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G2/
    """
    _id: Literal["G2"] = id_element(name="G2")

    SpecialIndicatorCode: X12ID = element(
        name="G201",
        description="Special Indicator Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="G202",
        description="Description",
        min_length=1,
        max_length=80,
    )
