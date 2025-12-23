# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class Q3(Segment):
    """
    Q3 - Arrival Details
    
    Description:
        To specify estimated arrival date and shipment method of payment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/Q3/
    """
    _id: Literal["Q3"] = id_element(name="Q3")

    Date: X12DT = element(
        name="Q301",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="Q302",
        description="Shipment Method of Payment",
        mandatory=True,
    )
