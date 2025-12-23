# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ACT(Segment):
    """
    ACT - Account Identification
    
    Description:
        To specify account information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ACT/
    """
    _id: Literal["ACT"] = id_element(name="ACT")

    AccountNumber: X12AN = element(
        name="ACT01",
        description="Account Number",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    Name: Optional[X12AN] = element(
        name="ACT02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="ACT03",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="ACT04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    AccountNumberQualifier: Optional[X12ID] = element(
        name="ACT05",
        description="Account Number Qualifier",
        min_length=1,
        max_length=3,
    )

    AccountNumber2: Optional[X12AN] = element(
        name="ACT06",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    Description: Optional[X12AN] = element(
        name="ACT07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="ACT08",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )

    BenefitStatusCode: Optional[X12ID] = element(
        name="ACT09",
        description="Benefit Status Code",
        min_length=1,
        max_length=1,
    )
