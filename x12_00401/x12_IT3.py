# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class IT3(Segment):
    """
    IT3 - Additional Item Data
    
    Description:
        To specify additional item details relating to variations between ordered and shipped quantities, or to specify alternate units of measures and quantities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IT3/
    """
    _id: Literal["IT3"] = id_element(name="IT3")

    UnitsShipped: Optional[X12R] = element(
        name="IT301",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    UnitCode: Optional[X12ID] = element(
        name="IT302",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    ShipmentOrderStatusCode: Optional[X12ID] = element(
        name="IT303",
        description="Shipment/Order Status Code",
        min_length=2,
        max_length=2,
    )

    QuantityDifference: Optional[X12R] = element(
        name="IT304",
        description="Quantity Difference",
        min_length=1,
        max_length=9,
    )

    ChangeReasonCode: Optional[X12ID] = element(
        name="IT305",
        description="Change Reason Code",
        min_length=2,
        max_length=2,
    )
