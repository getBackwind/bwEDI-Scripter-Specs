# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class P2(Segment):
    """
    P2 - Delivery Date Information
    
    Description:
        To specify delivery date
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/P2/
    """
    _id: Literal["P2"] = id_element(name="P2")

    PickupOrDeliveryCode: Optional[X12ID] = element(
        name="P201",
        description="Pickup or Delivery Code",
        min_length=1,
        max_length=2,
    )

    DeliveryDate: X12DT = element(
        name="P202",
        description="Delivery Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier: X12ID = element(
        name="P203",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )
