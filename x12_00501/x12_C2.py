# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class C2(Segment):
    """
    C2 - Bank ID
    
    Description:
        To specify data required for electronic payment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/C2/
    """
    _id: Literal["C2"] = id_element(name="C2")

    BankClientCode: X12ID = element(
        name="C201",
        description="Bank Client Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="C202",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="C203",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    ClientBankNumber: Optional[X12AN] = element(
        name="C204",
        description="Client Bank Number",
        min_length=3,
        max_length=9,
    )

    BankAccountNumber: Optional[X12AN] = element(
        name="C205",
        description="Bank Account Number",
        min_length=6,
        max_length=17,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="C206",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="C207",
        description="Date",
        min_length=8,
        max_length=8,
    )
