# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class ATA(Segment):
    """
    ATA - Beginning Segment for Motor Carrier Delivery Trailer Manifest
    
    Description:
        To transmit identifying numbers and other basic data relating to the Motor Carrier Delivery Trailer Manifest Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ATA/
    """
    _id: Literal["ATA"] = id_element(name="ATA")

    StandardCarrierAlphaCode: X12ID = element(
        name="ATA01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ReferenceIdentification: X12AN = element(
        name="ATA02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="ATA03",
        description="Date",
        min_length=8,
        max_length=8,
    )
