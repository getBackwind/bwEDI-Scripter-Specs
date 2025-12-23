# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class RIC(Segment):
    """
    RIC - Financial Return
    
    Description:
        To transmit information about the item being returned
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RIC/
    """
    _id: Literal["RIC"] = id_element(name="RIC")

    PaymentMethodCode: X12ID = element(
        name="RIC01",
        description="Payment Method Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    CodeListQualifierCode: X12ID = element(
        name="RIC02",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="RIC03",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: X12R = element(
        name="RIC04",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    CreditDebitFlagCode: X12ID = element(
        name="RIC05",
        description="Credit/Debit Flag Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AccountNumber: Optional[X12AN] = element(
        name="RIC06",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    AccountNumberQualifier: Optional[X12ID] = element(
        name="RIC07",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    DFIIDNumberQualifier: Optional[X12ID] = element(
        name="RIC08",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber: Optional[X12AN] = element(
        name="RIC09",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    AccountNumber2: Optional[X12AN] = element(
        name="RIC10",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    AccountNumberQualifier2: Optional[X12ID] = element(
        name="RIC11",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    DFIIDNumberQualifier2: Optional[X12ID] = element(
        name="RIC12",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber2: Optional[X12AN] = element(
        name="RIC13",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    AccountNumber3: Optional[X12AN] = element(
        name="RIC14",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    AccountNumberQualifier3: Optional[X12ID] = element(
        name="RIC15",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    DFIIDNumberQualifier3: Optional[X12ID] = element(
        name="RIC16",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber3: Optional[X12AN] = element(
        name="RIC17",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    Date: Optional[X12DT] = element(
        name="RIC18",
        description="Date",
        min_length=8,
        max_length=8,
    )
