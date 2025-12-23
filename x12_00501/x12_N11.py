# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class N11(Segment):
    """
    N11 - Store Location
    
    Description:
        To specify store numbers related to specific addresses for deliveries
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/N11/
    """
    _id: Literal["N11"] = id_element(name="N11")

    StoreNumber: X12AN = element(
        name="N1101",
        description="Store Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="N1102",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="N1103",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
