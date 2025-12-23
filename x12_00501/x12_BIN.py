# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn


class BIN(Segment):
    """
    BIN - Binary Data Segment
    
    Description:
        To transfer binary data in a single data segment and allow identification of the end of the data segment through a count; there is no identification of the internal structure of the binary data in this segment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BIN/
    """
    _id: Literal["BIN"] = id_element(name="BIN")

    LengthOfBinaryData: X12Nn = element(
        name="BIN01",
        description="Length of Binary Data",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    BinaryData: X12AN = element(
        name="BIN02",
        description="Binary Data",
        mandatory=True,
        min_length=1,
        max_length=1000000,
    )
