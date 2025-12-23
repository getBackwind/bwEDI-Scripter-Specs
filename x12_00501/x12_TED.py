# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class TED(Segment):
    """
    TED - Technical Error Description
    
    Description:
        To identify the error and, if feasible, the erroneous segment, or data element, or both
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TED/
    """
    _id: Literal["TED"] = id_element(name="TED")

    TED01: X12ID = element(
        name="TED01",
        description="Application Error Condition Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    TED02: Optional[X12AN] = element(
        name="TED02",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )

    SegmentIDCode: Optional[X12ID] = element(
        name="TED03",
        description="Segment ID Code",
        min_length=2,
        max_length=3,
    )

    SegmentPositionInTransactionSet: Optional[X12Nn] = element(
        name="TED04",
        description="Segment Position in Transaction Set",
        min_length=1,
        max_length=10,
    )

    CopyOfBadDataElement: Optional[X12AN] = element(
        name="TED07",
        description="Copy of Bad Data Element",
        min_length=1,
        max_length=99,
    )

    DataElementNewContent: Optional[X12AN] = element(
        name="TED08",
        description="Data Element New Content",
        min_length=1,
        max_length=99,
    )
