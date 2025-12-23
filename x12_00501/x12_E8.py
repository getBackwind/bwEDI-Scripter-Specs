# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class E8(Segment):
    """
    E8 - Blocking and Response Information
    
    Description:
        To identify a block of cars and the response information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E8/
    """
    _id: Literal["E8"] = id_element(name="E8")

    BlockIdentifier: Optional[X12AN] = element(
        name="E801",
        description="Block Identifier",
        min_length=1,
        max_length=12,
    )

    MovementAuthorityCode: Optional[X12ID] = element(
        name="E802",
        description="Movement Authority Code",
        min_length=1,
        max_length=2,
    )
