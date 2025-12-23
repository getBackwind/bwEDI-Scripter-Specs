# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PLI(Segment):
    """
    PLI - Previous Loan Information
    
    Description:
        To provide information about an existing loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PLI/
    """
    _id: Literal["PLI"] = id_element(name="PLI")

    LoanTypeCode: X12ID = element(
        name="PLI01",
        description="Loan Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: X12R = element(
        name="PLI02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    InterestRate: X12R = element(
        name="PLI03",
        description="Interest Rate",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="PLI04",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PLI05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PLI06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="PLI07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="PLI08",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="PLI09",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )
