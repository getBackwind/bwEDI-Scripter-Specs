# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class L3(Segment):
    """
    L3 - Total Weight and Charges
    
    Description:
        To specify the total shipment in terms of weight, volume, rates, charges, advances, and prepaid amounts applicable to one or more line items
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/L3/
    """
    _id: Literal["L3"] = id_element(name="L3")

    Weight: Optional[X12R] = element(
        name="L301",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="L302",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    FreightRate: Optional[X12R] = element(
        name="L303",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="L304",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    AmountCharged: Optional[X12Nn] = element(
        name="L305",
        description="Amount Charged",
        min_length=1,
        max_length=15,
    )

    Advances: Optional[X12Nn] = element(
        name="L306",
        description="Advances",
        min_length=1,
        max_length=9,
    )

    PrepaidAmount: Optional[X12Nn] = element(
        name="L307",
        description="Prepaid Amount",
        min_length=1,
        max_length=15,
    )

    SpecialChargeOrAllowanceCode: Optional[X12ID] = element(
        name="L308",
        description="Special Charge or Allowance Code",
        min_length=3,
        max_length=3,
    )

    Volume: Optional[X12R] = element(
        name="L309",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="L310",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="L311",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="L312",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    TariffNumber: Optional[X12AN] = element(
        name="L313",
        description="Tariff Number",
        min_length=1,
        max_length=7,
    )

    DeclaredValue: Optional[X12Nn] = element(
        name="L314",
        description="Declared Value",
        min_length=2,
        max_length=12,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="L315",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )
