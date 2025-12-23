# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SAD(Segment):
    """
    SAD - Student Award Detail
    
    Description:
        To provide detail concerning a student award
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SAD/
    """
    _id: Literal["SAD"] = id_element(name="SAD")

    StatusReasonCode: Optional[X12ID] = element(
        name="SAD01",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    InterestRate: Optional[X12R] = element(
        name="SAD02",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="SAD03",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="SAD04",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="SAD05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="SAD06",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="SAD07",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
