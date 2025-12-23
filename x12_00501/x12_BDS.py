# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class BDS(Segment):
    """
    BDS - Binary Data Structure
    
    Description:
        To transfer binary data in a single data segment, convey a critical filter for transmission and allow identification of the end of the data segment through a count; there is no identification of the internal structure of the binary data in this segment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BDS/
    """
    _id: Literal["BDS"] = id_element(name="BDS")

    FilterIDCode: X12ID = element(
        name="BDS01",
        description="Filter ID Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    LengthOfBinaryData: X12Nn = element(
        name="BDS02",
        description="Length of Binary Data",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    BinaryData: X12AN = element(
        name="BDS03",
        description="Binary Data",
        mandatory=True,
        min_length=1,
        max_length=1000000,
    )
