# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class GR(Segment):
    """
    GR - Guarantee Result Detail
    
    Description:
        To provide information related to the disposition of a student loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/GR/
    """
    _id: Literal["GR"] = id_element(name="GR")

    LoanTypeCode: X12ID = element(
        name="GR01",
        description="Loan Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    LoanStatusCode: X12ID = element(
        name="GR02",
        description="Loan Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="GR03",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="GR04",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    DateTimePeriodFormatQualifier2: X12ID = element(
        name="GR05",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: X12AN = element(
        name="GR06",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    DateTimePeriodFormatQualifier3: Optional[X12ID] = element(
        name="GR07",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="GR08",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="GR09",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    InterestRate: Optional[X12R] = element(
        name="GR10",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="GR11",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )

    InterestRate2: Optional[X12R] = element(
        name="GR12",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="GR13",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="GR14",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    DateTimePeriodFormatQualifier4: Optional[X12ID] = element(
        name="GR15",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod4: Optional[X12AN] = element(
        name="GR16",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="GR17",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="GR18",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="GR19",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="GR20",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="GR21",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
