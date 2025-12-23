# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class L8(Segment):
    """
    L8 - Line Item Subtotal
    
    Description:
        To specify line item subtotals
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/L8/
    """
    _id: Literal["L8"] = id_element(name="L8")

    BilledRatedAsQuantity: Optional[X12R] = element(
        name="L801",
        description="Billed/Rated-as Quantity",
        min_length=1,
        max_length=11,
    )

    BilledRatedAsQualifier: Optional[X12ID] = element(
        name="L802",
        description="Billed/Rated-as Qualifier",
        min_length=2,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="L803",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="L804",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="L805",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    FreightRate: Optional[X12R] = element(
        name="L806",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="L807",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Amount: Optional[X12Nn] = element(
        name="L808",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    SpecialChargeOrAllowanceCode: Optional[X12ID] = element(
        name="L809",
        description="Special Charge or Allowance Code",
        min_length=3,
        max_length=3,
    )

    SpecialChargeDescription: Optional[X12AN] = element(
        name="L810",
        description="Special Charge Description",
        min_length=2,
        max_length=25,
    )

    ChargeMethodOfPayment: Optional[X12ID] = element(
        name="L811",
        description="Charge Method of Payment",
    )
