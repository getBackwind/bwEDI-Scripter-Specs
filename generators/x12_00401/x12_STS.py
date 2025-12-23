# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class STS(Segment):
    """
    STS - Interchange Status Segment
    
    Description:
        To identify activity taken with an interchange
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/STS/
    """
    _id: Literal["STS"] = id_element(name="STS")

    TimeCode: Optional[X12ID] = element(
        name="STS04",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
