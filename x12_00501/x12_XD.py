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
        https://www.kasoftware.com/schema/edi/x12/00501/segments/XD/
    """
    _id: Literal["XD"] = id_element(name="XD")

    SwitchTypeCode: Optional[X12ID] = element(
        name="XD01",
        description="Switch Type Code",
        min_length=2,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="XD02",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="XD03",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="XD04",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    RejectReasonCode: Optional[X12ID] = element(
        name="XD05",
        description="Reject Reason Code",
        min_length=2,
        max_length=2,
    )
