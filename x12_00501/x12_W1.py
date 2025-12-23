# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class W1(Segment):
    """
    W1 - Block Identification
    
    Description:
        To identify the block identification of a specific cut of cars relating to this interchange report
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W1/
    """
    _id: Literal["W1"] = id_element(name="W1")

    BlockIdentifier: X12AN = element(
        name="W101",
        description="Block Identifier",
        mandatory=True,
        min_length=1,
        max_length=12,
    )
