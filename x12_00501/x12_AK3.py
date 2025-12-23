# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class AK3(Segment):
    """
    AK3 - Data Segment Note
    
    Description:
        To report errors in a data segment and identify the location of the data segment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AK3/
    """
    _id: Literal["AK3"] = id_element(name="AK3")

    SegmentID: X12ID = element(
        name="AK301",
        description="Segment ID Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    SegmentPosition: X12Nn = element(
        name="AK302",
        description="Segment Position in Transaction Set",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    LoopID: Optional[X12AN] = element(
        name="AK303",
        description="Loop Identifier Code",
        min_length=1,
        max_length=4,
    )

    ErrorCode: Optional[X12ID] = element(
        name="AK304",
        description="Segment Syntax Error Code",
        min_length=1,
        max_length=1,
    )
