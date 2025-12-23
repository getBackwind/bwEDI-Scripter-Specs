# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class K1(Segment):
    """
    K1 - Remarks
    
    Description:
        To transmit information in a free-form format for comment or special instruction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/K1/
    """
    _id: Literal["K1"] = id_element(name="K1")

    FreeFormMessage: X12AN = element(
        name="K101",
        description="Free-Form Message",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    FreeFormMessage2: Optional[X12AN] = element(
        name="K102",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )
