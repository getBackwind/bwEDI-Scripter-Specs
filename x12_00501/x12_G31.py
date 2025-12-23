# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G31(Segment):
    """
    G31 - Total Invoice Quantity
    
    Description:
        To specify summary details of total items shipped in terms of quantity, weight, and volume, and to specify payment method
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G31/
    """
    _id: Literal["G31"] = id_element(name="G31")

    NumberOfUnitsShipped: X12R = element(
        name="G3101",
        description="Number of Units Shipped",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="G3102",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="G3103",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G3104",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="G3105",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="G3106",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    OrderSizingFactor: Optional[X12R] = element(
        name="G3107",
        description="Order Sizing Factor",
        min_length=1,
        max_length=10,
    )

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="G3108",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="G3109",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="G3110",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Weight2: Optional[X12R] = element(
        name="G3111",
        description="Weight",
        min_length=1,
        max_length=10,
    )
