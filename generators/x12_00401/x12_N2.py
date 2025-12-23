# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class N2(Segment):
    """
    N2 - Additional Name Information
    
    Description:
        To specify additional names or those longer than 35 characters in length
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N2/
    """
    _id: Literal["N2"] = id_element(name="N2")

    Name2: X12AN = element(
        name="N201",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    Name3: Optional[X12AN] = element(
        name="N202",
        description="Name",
        min_length=1,
        max_length=60,
    )
