# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class CTP(Segment):
    """
    CTP - Pricing Information
    
    Description:
        To specify pricing information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CTP/
    """
    _id: Literal["CTP"] = id_element(name="CTP")

    ClassOfTradeCode: Optional[X12ID] = element(
        name="CTP01",
        description="Class of Trade Code",
        min_length=2,
        max_length=2,
    )

    PriceCode: Optional[X12ID] = element(
        name="CTP02",
        description="Price Identifier Code",
        min_length=3,
        max_length=3,
    )

    Price: Optional[X12R] = element(
        name="CTP03",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    Quantity: Optional[X12R] = element(
        name="CTP04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PriceMultiplierQualifier: Optional[X12ID] = element(
        name="CTP06",
        description="Price Multiplier Qualifier",
        min_length=3,
        max_length=3,
    )

    Multiplier: Optional[X12R] = element(
        name="CTP07",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CTP08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    BasisOfUnitPriceCode: Optional[X12ID] = element(
        name="CTP09",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )

    ConditionValue: Optional[X12AN] = element(
        name="CTP10",
        description="Condition Value",
        min_length=1,
        max_length=10,
    )

    MultiplePriceQuantity: Optional[X12Nn] = element(
        name="CTP11",
        description="Multiple Price Quantity",
        min_length=1,
        max_length=2,
    )
