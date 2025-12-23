# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class L1(Segment):
    """
    L1 - Rate and Charges
    
    Description:
        To specify rate and charges detail relative to a line item including freight charges, advances, special charges, and entitlements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/L1/
    """
    _id: Literal["L1"] = id_element(name="L1")

    LadingLineItemNumber: Optional[X12Nn] = element(
        name="L101",
        description="Lading Line Item Number",
        min_length=1,
        max_length=3,
    )

    FreightRate: Optional[X12R] = element(
        name="L102",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="L103",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    AmountCharged: Optional[X12Nn] = element(
        name="L104",
        description="Amount Charged",
        min_length=1,
        max_length=15,
    )

    Advances: Optional[X12Nn] = element(
        name="L105",
        description="Advances",
        min_length=1,
        max_length=9,
    )

    PrepaidAmount: Optional[X12Nn] = element(
        name="L106",
        description="Prepaid Amount",
        min_length=1,
        max_length=15,
    )

    RateCombinationPointCode: Optional[X12AN] = element(
        name="L107",
        description="Rate Combination Point Code",
        min_length=3,
        max_length=9,
    )

    SpecialChargeOrAllowanceCode: Optional[X12ID] = element(
        name="L108",
        description="Special Charge or Allowance Code",
        min_length=3,
        max_length=3,
    )

    RateClassCode: Optional[X12ID] = element(
        name="L109",
        description="Rate Class Code",
        min_length=1,
        max_length=3,
    )

    EntitlementCode: Optional[X12ID] = element(
        name="L110",
        description="Entitlement Code",
        min_length=1,
        max_length=1,
    )

    ChargeMethodOfPayment: Optional[X12ID] = element(
        name="L111",
        description="Charge Method of Payment",
    )

    SpecialChargeDescription: Optional[X12AN] = element(
        name="L112",
        description="Special Charge Description",
        min_length=2,
        max_length=25,
    )

    TariffApplicationCode: Optional[X12ID] = element(
        name="L113",
        description="Tariff Application Code",
        min_length=1,
        max_length=1,
    )

    DeclaredValue: Optional[X12Nn] = element(
        name="L114",
        description="Declared Value",
        min_length=2,
        max_length=12,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="L115",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    LadingLiabilityCode: Optional[X12ID] = element(
        name="L116",
        description="Lading Liability Code",
        min_length=1,
        max_length=1,
    )

    BilledRatedAsQuantity: Optional[X12R] = element(
        name="L117",
        description="Billed/Rated-as Quantity",
        min_length=1,
        max_length=11,
    )

    BilledRatedAsQualifier: Optional[X12ID] = element(
        name="L118",
        description="Billed/Rated-as Qualifier",
        min_length=2,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="L119",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="L120",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    Amount: Optional[X12Nn] = element(
        name="L121",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    LadingValue: Optional[X12R] = element(
        name="L122",
        description="Lading Value",
        min_length=2,
        max_length=9,
    )
