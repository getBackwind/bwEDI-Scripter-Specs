# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class XD(Segment):
    """
    XD - Placement/Pull Data
    
    Description:
        To define the status and positioning of cars within the location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/XD/
    """
    _id: Literal["XD"] = id_element(name="XD")

    SwitchTypeCode: X12ID = element(
        name="XD01",
        description="Switch Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Zone: Optional[X12AN] = element(
        name="XD02",
        description="Zone",
        min_length=2,
        max_length=3,
    )

    Track: Optional[X12AN] = element(
        name="XD03",
        description="Track",
        min_length=2,
        max_length=3,
    )

    Spot: Optional[X12AN] = element(
        name="XD04",
        description="Spot",
        min_length=2,
        max_length=3,
    )

    Spot2: Optional[X12AN] = element(
        name="XD05",
        description="Spot",
        min_length=2,
        max_length=3,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="XD06",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="XD07",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    RejectReasonCode: Optional[X12ID] = element(
        name="XD08",
        description="Reject Reason Code",
        min_length=2,
        max_length=2,
    )
