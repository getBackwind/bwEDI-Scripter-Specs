# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn


class S2(Segment):
    """
    S2 - Stop-off Address
    
    Description:
        To specify the address of the stop-off party
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/S2/
    """
    _id: Literal["S2"] = id_element(name="S2")

    StopSequenceNumber: X12Nn = element(
        name="S201",
        description="Stop Sequence Number",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    AddressInformation: X12AN = element(
        name="S202",
        description="Address Information",
        mandatory=True,
        min_length=1,
        max_length=55,
    )

    AddressInformation2: Optional[X12AN] = element(
        name="S203",
        description="Address Information",
        min_length=1,
        max_length=55,
    )
