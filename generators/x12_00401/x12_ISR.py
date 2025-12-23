# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class ISR(Segment):
    """
    ISR - Item Status Report
    
    Description:
        To specify detailed purchase order/item status
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ISR/
    """
    _id: Literal["ISR"] = id_element(name="ISR")

    OrderStatusCode: X12ID = element(
        name="ISR01",
        description="Shipment/Order Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="ISR02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="ISR03",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
