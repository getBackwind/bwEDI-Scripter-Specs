# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class SUM(Segment):
    """
    SUM - Academic Summary
    
    Description:
        To provide summary information for an academic session, a postsecondary degree, or for the entire student academic record
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SUM/
    """
    _id: Literal["SUM"] = id_element(name="SUM")

    AcademicCreditTypeCode: Optional[X12ID] = element(
        name="SUM01",
        description="Academic Credit Type Code",
        min_length=1,
        max_length=1,
    )

    AcademicGradeOrCourseLevelCode: Optional[X12ID] = element(
        name="SUM02",
        description="Academic Grade or Course Level Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SUM03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="SUM04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="SUM05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="SUM06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    RangeMinimum: Optional[X12R] = element(
        name="SUM07",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="SUM08",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    AcademicGradePointAverage: Optional[X12R] = element(
        name="SUM09",
        description="Academic Grade Point Average",
        min_length=1,
        max_length=6,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SUM10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ClassRank: Optional[X12Nn] = element(
        name="SUM11",
        description="Class Rank",
        min_length=1,
        max_length=4,
    )

    Quantity4: Optional[X12R] = element(
        name="SUM12",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="SUM13",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="SUM14",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    NumberOfDays: Optional[X12Nn] = element(
        name="SUM15",
        description="Number of Days",
        min_length=1,
        max_length=3,
    )

    Quantity5: Optional[X12R] = element(
        name="SUM16",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity6: Optional[X12R] = element(
        name="SUM17",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AcademicSummarySource: Optional[X12ID] = element(
        name="SUM18",
        description="Academic Summary Source",
    )
