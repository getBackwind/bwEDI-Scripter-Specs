# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12TM


class WS(Segment):
    """
    WS - Work Schedule
    
    Description:
        To specify an individual's work schedule
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/WS/
    """
    _id: Literal["WS"] = id_element(name="WS")

    ShipDeliveryOrCalendarPatternCode: X12ID = element(
        name="WS01",
        description="Ship/Delivery or Calendar Pattern Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="WS02",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="WS03",
        description="Time",
        min_length=4,
        max_length=8,
    )
