# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class F01(Segment):
    """
    F01 - Identification of Claim (Claimant Originated)
    
    Description:
        To identify a loss or damage claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/F01/
    """
    _id: Literal["F01"] = id_element(name="F01")

    Date: X12DT = element(
        name="F0101",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: X12AN = element(
        name="F0102",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Amount: X12Nn = element(
        name="F0103",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="F0104",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    SupportingEvidenceCode: X12ID = element(
        name="F0105",
        description="Supporting Evidence Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="F0106",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    ExchangeRate: Optional[X12R] = element(
        name="F0107",
        description="Exchange Rate",
        min_length=4,
        max_length=10,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="F0108",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="F0109",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
