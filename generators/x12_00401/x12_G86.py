# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class G86(Segment):
    """
    G86 - Signature
    
    Description:
        To transmit an electronic identity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G86/
    """
    _id: Literal["G86"] = id_element(name="G86")

    Signature: Optional[X12AN] = element(
        name="G8601",
        description="Signature",
        min_length=1,
        max_length=12,
    )

    Name: Optional[X12AN] = element(
        name="G8602",
        description="Name",
        min_length=1,
        max_length=60,
    )
