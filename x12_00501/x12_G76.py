# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class G76(Segment):
    """
    G76 - Total Purchase Order
    
    Description:
        To specify summary details of total items shipped in terms of quantity, weight, and volume, and to specify payment method
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G76/
    """
    _id: Literal["G76"] = id_element(name="G76")

    Quantity: X12R = element(
        name="G7601",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: X12ID = element(
        name="G7602",
        description="Unit or Basis for Measurement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="G7603",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode2: Optional[X12ID] = element(
        name="G7604",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="G7605",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode3: Optional[X12ID] = element(
        name="G7606",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    OrderSizingFactor: Optional[X12R] = element(
        name="G7607",
        description="Order Sizing Factor",
        min_length=1,
        max_length=10,
    )

    Amount: Optional[X12Nn] = element(
        name="G7608",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="G7609",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="G7610",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )
