# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class W76(Segment):
    """
    W76 - Total Shipping Order
    
    Description:
        To specify summary details of total items shipped in terms of quantity, weight, and volume
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W76/
    """
    _id: Literal["W76"] = id_element(name="W76")

    Quantity: X12R = element(
        name="W7601",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Weight: Optional[X12R] = element(
        name="W7602",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="W7603",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="W7604",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="W7605",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    OrderSizingFactor: Optional[X12R] = element(
        name="W7606",
        description="Order Sizing Factor",
        min_length=1,
        max_length=10,
    )
