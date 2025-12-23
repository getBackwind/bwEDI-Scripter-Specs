# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12TM


class DH(Segment):
    """
    DH - Dealer Hours
    
    Description:
        To provide a carrier with information about the business hours during which deliveries will be received by the dealer
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DH/
    """
    _id: Literal["DH"] = id_element(name="DH")

    ShipDeliveryOrCalendarPatternCode: X12ID = element(
        name="DH01",
        description="Ship/Delivery or Calendar Pattern Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Time: X12TM = element(
        name="DH02",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    Time2: X12TM = element(
        name="DH03",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )
