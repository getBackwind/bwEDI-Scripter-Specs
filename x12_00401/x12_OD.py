# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class OD(Segment):
    """
    OD - Origin and Destination
    
    Description:
        To identify the origin and destination of a shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/OD/
    """
    _id: Literal["OD"] = id_element(name="OD")

    StandardPointLocationCode: X12ID = element(
        name="OD01",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    StandardPointLocationCode2: X12ID = element(
        name="OD02",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="OD03",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="OD04",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
