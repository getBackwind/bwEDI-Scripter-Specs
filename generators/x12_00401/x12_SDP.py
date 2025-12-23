# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class SDP(Segment):
    """
    SDP - Ship/Delivery Pattern
    
    Description:
        To identify specific ship/delivery requirements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SDP/
    """
    _id: Literal["SDP"] = id_element(name="SDP")

    ShipDeliveryOrCalendarPatternCode: X12ID = element(
        name="SDP01",
        description="Ship/Delivery or Calendar Pattern Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ShipDeliveryPatternTimeCode: X12ID = element(
        name="SDP02",
        description="Ship/Delivery Pattern Time Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ShipDeliveryOrCalendarPatternCode2: Optional[X12ID] = element(
        name="SDP03",
        description="Ship/Delivery or Calendar Pattern Code",
        min_length=1,
        max_length=2,
    )

    ShipDeliveryPatternTimeCode2: Optional[X12ID] = element(
        name="SDP04",
        description="Ship/Delivery Pattern Time Code",
        min_length=1,
        max_length=1,
    )

    ShipDeliveryOrCalendarPatternCode3: Optional[X12ID] = element(
        name="SDP05",
        description="Ship/Delivery or Calendar Pattern Code",
        min_length=1,
        max_length=2,
    )

    ShipDeliveryPatternTimeCode3: Optional[X12ID] = element(
        name="SDP06",
        description="Ship/Delivery Pattern Time Code",
        min_length=1,
        max_length=1,
    )

    ShipDeliveryOrCalendarPatternCode4: Optional[X12ID] = element(
        name="SDP07",
        description="Ship/Delivery or Calendar Pattern Code",
        min_length=1,
        max_length=2,
    )

    ShipDeliveryPatternTimeCode4: Optional[X12ID] = element(
        name="SDP08",
        description="Ship/Delivery Pattern Time Code",
        min_length=1,
        max_length=1,
    )
