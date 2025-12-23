# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class DEF(Segment):
    """
    DEF - Delayed Repayment
    
    Description:
        To provide information related to student loan delayed repayment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DEF/
    """
    _id: Literal["DEF"] = id_element(name="DEF")

    DelayedRepaymentQualifierCode: X12ID = element(
        name="DEF01",
        description="Delayed Repayment Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DelayedRepaymentReasonCode: X12ID = element(
        name="DEF02",
        description="Delayed Repayment Reason Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="DEF03",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="DEF04",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    InterestPaymentCode: Optional[X12ID] = element(
        name="DEF05",
        description="Interest Payment Code",
        min_length=1,
        max_length=1,
    )
