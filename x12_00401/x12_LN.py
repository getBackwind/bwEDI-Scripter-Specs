# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LN(Segment):
    """
    LN - Loan Information
    
    Description:
        To specify information about the loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LN/
    """
    _id: Literal["LN"] = id_element(name="LN")

    ReferenceIdentification: X12AN = element(
        name="LN01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: X12R = element(
        name="LN02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="LN03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="LN04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="LN05",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="LN06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="LN07",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LN08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LoanPurposeCode: Optional[X12ID] = element(
        name="LN09",
        description="Loan Purpose Code",
        min_length=2,
        max_length=2,
    )

    LoanPaymentTypeCode: Optional[X12ID] = element(
        name="LN10",
        description="Loan Payment Type Code",
        min_length=2,
        max_length=2,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="LN11",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )
