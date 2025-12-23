# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class IK3(Segment):
    """
    IK3 - Implementation Data Segment Note
    
    Description:
        To report implementation errors in a data segment and identify the location of the data segment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IK3/
    """
    _id: Literal["IK3"] = id_element(name="IK3")

    SegmentIDCode: X12ID = element(
        name="IK301",
        description="Segment ID Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    SegmentPositionInTransactionSet: X12Nn = element(
        name="IK302",
        description="Segment Position in Transaction Set",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    LoopIdentifierCode: Optional[X12AN] = element(
        name="IK303",
        description="Loop Identifier Code",
        min_length=1,
        max_length=4,
    )

    ImplementationSegmentSyntaxErrorCode: Optional[X12ID] = element(
        name="IK304",
        description="Implementation Segment Syntax Error Code",
        min_length=1,
        max_length=2,
    )
