# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class IRP(Segment):
    """
    IRP - Report Selection Segment
    
    Description:
        To identify report selection criteria
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IRP/
    """
    _id: Literal["IRP"] = id_element(name="IRP")

    ShipDeliveryOrCalendarPatternCode: Optional[X12ID] = element(
        name="IRP07",
        description="Ship/Delivery or Calendar Pattern Code",
        min_length=1,
        max_length=2,
    )
