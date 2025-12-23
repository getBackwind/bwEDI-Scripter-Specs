# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class AT4(Segment):
    """
    AT4 - Bill of Lading Description
    
    Description:
        To specify the lading description
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AT4/
    """
    _id: Literal["AT4"] = id_element(name="AT4")

    LadingDescription: X12AN = element(
        name="AT401",
        description="Lading Description",
        mandatory=True,
        min_length=1,
        max_length=50,
    )
