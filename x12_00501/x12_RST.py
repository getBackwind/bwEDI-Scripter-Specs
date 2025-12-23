# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class RST(Segment):
    """
    RST - Carrier Restriction
    
    Description:
        To transmit the carrier's service restrictions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RST/
    """
    _id: Literal["RST"] = id_element(name="RST")

    CarrierRestrictionCode: Optional[X12AN] = element(
        name="RST01",
        description="Carrier Restriction Code",
        min_length=1,
        max_length=10,
    )

    Description: Optional[X12AN] = element(
        name="RST02",
        description="Description",
        min_length=1,
        max_length=80,
    )
