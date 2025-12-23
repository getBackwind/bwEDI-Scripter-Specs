# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RDR(Segment):
    """
    RDR - Return Disposition Reason
    
    Description:
        To indicate the disposition of the item, the reason for return by the returnee, the response to the reason for return, and whether the item was used
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RDR/
    """
    _id: Literal["RDR"] = id_element(name="RDR")

    ReturnsDispositionCode: Optional[X12ID] = element(
        name="RDR01",
        description="Returns Disposition Code",
        min_length=2,
        max_length=2,
    )

    ReturnRequestReasonCode: Optional[X12ID] = element(
        name="RDR02",
        description="Return Request Reason Code",
        min_length=2,
        max_length=2,
    )

    ReturnResponseReasonCode: Optional[X12ID] = element(
        name="RDR03",
        description="Return Response Reason Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="RDR04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="RDR05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
