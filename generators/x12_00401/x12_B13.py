# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class B13(Segment):
    """
    B13 - Beginning Segment for Appointment Schedule
    
    Description:
        To transmit identifying numbers and other basic data relating to the Appointment Schedule transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/B13/
    """
    _id: Literal["B13"] = id_element(name="B13")

    ReferenceIdentification: X12AN = element(
        name="B1301",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="B1302",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
