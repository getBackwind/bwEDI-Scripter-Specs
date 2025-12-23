# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class CTX(Segment):
    """
    CTX - Context
    
    Description:
        To identify the component data element position within the composite that is in error
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CTX/
    """
    _id: Literal["CTX"] = id_element(name="CTX")

    SegmentIDCode: Optional[X12ID] = element(
        name="CTX02",
        description="Segment ID Code",
        min_length=2,
        max_length=3,
    )

    SegmentPositionInTransactionSet: Optional[X12Nn] = element(
        name="CTX03",
        description="Segment Position in Transaction Set",
        min_length=1,
        max_length=10,
    )

    LoopIdentifierCode: Optional[X12AN] = element(
        name="CTX04",
        description="Loop Identifier Code",
        min_length=1,
        max_length=4,
    )
