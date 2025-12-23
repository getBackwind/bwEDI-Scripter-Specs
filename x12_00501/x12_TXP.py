# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class TXP(Segment):
    """
    TXP - Tax Payment
    
    Description:
        To identify tax payment data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TXP/
    """
    _id: Literal["TXP"] = id_element(name="TXP")

    TaxIdentificationNumber: X12AN = element(
        name="TXP01",
        description="Tax Identification Number",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    TaxPaymentTypeCode: X12ID = element(
        name="TXP02",
        description="Tax Payment Type Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    Date: X12DT = element(
        name="TXP03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    TaxInformationIdentificationNumber: X12AN = element(
        name="TXP04",
        description="Tax Information Identification Number",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    TaxAmount: X12Nn = element(
        name="TXP05",
        description="Tax Amount",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    TaxInformationIdentificationNumber2: Optional[X12AN] = element(
        name="TXP06",
        description="Tax Information Identification Number",
        min_length=1,
        max_length=30,
    )

    TaxAmount2: Optional[X12Nn] = element(
        name="TXP07",
        description="Tax Amount",
        min_length=1,
        max_length=10,
    )

    TaxInformationIdentificationNumber3: Optional[X12AN] = element(
        name="TXP08",
        description="Tax Information Identification Number",
        min_length=1,
        max_length=30,
    )

    TaxAmount3: Optional[X12Nn] = element(
        name="TXP09",
        description="Tax Amount",
        min_length=1,
        max_length=10,
    )

    TaxpayerVerification: Optional[X12AN] = element(
        name="TXP10",
        description="Taxpayer Verification",
        min_length=1,
        max_length=6,
    )
