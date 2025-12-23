# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PSA(Segment):
    """
    PSA - Partner Share Accounting
    
    Description:
        To communicate the percentage share of the project that a particular owner has to pay
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PSA/
    """
    _id: Literal["PSA"] = id_element(name="PSA")

    IdentificationCodeQualifier: X12ID = element(
        name="PSA01",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="PSA02",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    OwnersShare: X12R = element(
        name="PSA03",
        description="Owners Share",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PSA04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="PSA05",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )
