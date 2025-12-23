# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CDD(Segment):
    """
    CDD - Credit/Debit Adjustment Detail
    
    Description:
        To provide information relative to a line item adjustment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CDD/
    """
    _id: Literal["CDD"] = id_element(name="CDD")

    AdjustmentReasonCode: X12ID = element(
        name="CDD01",
        description="Adjustment Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CreditDebitFlagCode: X12ID = element(
        name="CDD02",
        description="Credit/Debit Flag Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="CDD03",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Amount: Optional[X12Nn] = element(
        name="CDD04",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CDD05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    PriceBracketIdentifier: Optional[X12AN] = element(
        name="CDD06",
        description="Price Bracket Identifier",
        min_length=1,
        max_length=3,
    )

    CreditDebitQuantity: Optional[X12R] = element(
        name="CDD07",
        description="Credit/Debit Quantity",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="CDD08",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    UnitPriceDifference: Optional[X12R] = element(
        name="CDD09",
        description="Unit Price Difference",
        min_length=1,
        max_length=15,
    )

    PriceIdentifierCode: Optional[X12ID] = element(
        name="CDD10",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    UnitPrice: Optional[X12R] = element(
        name="CDD11",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    PriceIdentifierCode2: Optional[X12ID] = element(
        name="CDD12",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    UnitPrice2: Optional[X12R] = element(
        name="CDD13",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )
