# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class K2(Segment):
    """
    K2 - Administrative Message
    
    Description:
        To transmit information in a free-form format for comment or special instruction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/K2/
    """
    _id: Literal["K2"] = id_element(name="K2")

    Description: X12AN = element(
        name="K201",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
