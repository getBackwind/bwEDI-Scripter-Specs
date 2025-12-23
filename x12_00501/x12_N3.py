# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class N3(Segment):
    """
    N3 - Party Location
    
    Description:
        To specify the location of the named party
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/N3/
    """
    _id: Literal["N3"] = id_element(name="N3")

    AddressLine1: X12AN = element(
        name="N301",
        description="Address Information",
        mandatory=True,
        min_length=1,
        max_length=55,
    )

    AddressLine2: Optional[X12AN] = element(
        name="N302",
        description="Address Information",
        min_length=1,
        max_length=55,
    )
