# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PDL(Segment):
    """
    PDL - Payment Details
    
    Description:
        To transmit information required to establish payment or remittance activity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PDL/
    """
    _id: Literal["PDL"] = id_element(name="PDL")

    PaymentMethodCode: X12ID = element(
        name="PDL01",
        description="Payment Method Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="PDL02",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PDL03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="PDL04",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    CreditDebitFlagCode: Optional[X12ID] = element(
        name="PDL05",
        description="Credit/Debit Flag Code",
        min_length=1,
        max_length=1,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="PDL06",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    DFIIDNumberQualifier: Optional[X12ID] = element(
        name="PDL07",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber: Optional[X12AN] = element(
        name="PDL08",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    AccountNumberQualifier: Optional[X12ID] = element(
        name="PDL09",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    AccountNumber: Optional[X12AN] = element(
        name="PDL10",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PDL11",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PDL12",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
