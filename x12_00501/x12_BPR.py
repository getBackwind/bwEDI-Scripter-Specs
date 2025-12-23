# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class BPR(Segment):
    """
    BPR - Beginning Segment for Payment Order/Remittance Advice
    
    Description:
        To indicate the beginning of a Payment Order/Remittance Advice Transaction Set and total payment amount, or to enable related transfer of funds and/or information from payer to payee to occur
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BPR/
    """
    _id: Literal["BPR"] = id_element(name="BPR")

    TransactionHandlingCode: X12ID = element(
        name="BPR01",
        description="Transaction Handling Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MonetaryAmount: X12R = element(
        name="BPR02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    CreditDebitFlagCode: X12ID = element(
        name="BPR03",
        description="Credit/Debit Flag Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PaymentMethodCode: X12ID = element(
        name="BPR04",
        description="Payment Method Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    PaymentFormatCode: Optional[X12ID] = element(
        name="BPR05",
        description="Payment Format Code",
        min_length=3,
        max_length=3,
    )

    DFIIDNumberQualifier: Optional[X12ID] = element(
        name="BPR06",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber: Optional[X12AN] = element(
        name="BPR07",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    AccountNumberQualifier: Optional[X12ID] = element(
        name="BPR08",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    AccountNumber: Optional[X12AN] = element(
        name="BPR09",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    OriginatingCompanyIdentifier: Optional[X12AN] = element(
        name="BPR10",
        description="Originating Company Identifier",
        min_length=10,
        max_length=10,
    )

    OriginatingCompanySupplementalCode: Optional[X12AN] = element(
        name="BPR11",
        description="Originating Company Supplemental Code",
        min_length=9,
        max_length=9,
    )

    DFIIDNumberQualifier2: Optional[X12ID] = element(
        name="BPR12",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber2: Optional[X12AN] = element(
        name="BPR13",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    AccountNumberQualifier2: Optional[X12ID] = element(
        name="BPR14",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    AccountNumber2: Optional[X12AN] = element(
        name="BPR15",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    Date: Optional[X12DT] = element(
        name="BPR16",
        description="Date",
        min_length=8,
        max_length=8,
    )

    BusinessFunctionCode: Optional[X12ID] = element(
        name="BPR17",
        description="Business Function Code",
        min_length=3,
        max_length=3,
    )

    DFIIDNumberQualifier3: Optional[X12ID] = element(
        name="BPR18",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber3: Optional[X12AN] = element(
        name="BPR19",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    AccountNumberQualifier3: Optional[X12ID] = element(
        name="BPR20",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    AccountNumber3: Optional[X12AN] = element(
        name="BPR21",
        description="Account Number",
        min_length=1,
        max_length=35,
    )
