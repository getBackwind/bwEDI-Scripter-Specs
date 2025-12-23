# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class LE(Segment):
    """
    LE - Loop Trailer
    
    Description:
        To indicate that the loop immediately preceding this segment is complete
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LE/
    """
    _id: Literal["LE"] = id_element(name="LE")

    LoopID: X12AN = element(
        name="LE01",
        description="Loop Identifier Code",
        mandatory=True,
        min_length=1,
        max_length=6,
    )
