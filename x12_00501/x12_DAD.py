# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class DAD(Segment):
    """
    DAD - Debit Authorization Detail
    
    Description:
        To provide detail information about the debit authorization
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DAD/
    """
    _id: Literal["DAD"] = id_element(name="DAD")

    ActionCode: X12ID = element(
        name="DAD01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    TransactionHandlingCode: X12ID = element(
        name="DAD02",
        description="Transaction Handling Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="DAD03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="DAD04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    OriginatingCompanyIdentifier: Optional[X12AN] = element(
        name="DAD05",
        description="Originating Company Identifier",
        min_length=10,
        max_length=10,
    )

    OriginatingCompanySupplementalCode: Optional[X12AN] = element(
        name="DAD06",
        description="Originating Company Supplemental Code",
        min_length=9,
        max_length=9,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="DAD07",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="DAD08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="DAD09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="DAD10",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    DFIIDNumberQualifier: Optional[X12ID] = element(
        name="DAD11",
        description="(DFI) ID Number Qualifier",
        min_length=2,
        max_length=2,
    )

    DFIIdentificationNumber: Optional[X12AN] = element(
        name="DAD12",
        description="(DFI) Identification Number",
        min_length=3,
        max_length=12,
    )

    AccountNumber: Optional[X12AN] = element(
        name="DAD13",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    Number: Optional[X12Nn] = element(
        name="DAD14",
        description="Number",
        min_length=1,
        max_length=9,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="DAD15",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )
