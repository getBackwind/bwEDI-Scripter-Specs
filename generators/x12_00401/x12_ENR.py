# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ENR(Segment):
    """
    ENR - School Enrollment Information
    
    Description:
        To provide school data relative to the applicant or the student
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ENR/
    """
    _id: Literal["ENR"] = id_element(name="ENR")

    StatusReasonCode: X12ID = element(
        name="ENR01",
        description="Status Reason Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="ENR02",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="ENR03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="ENR04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MajorCourseOfStudy: Optional[X12ID] = element(
        name="ENR05",
        description="Major Course of Study",
    )

    RangeMinimum: Optional[X12R] = element(
        name="ENR06",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="ENR07",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    AcademicGradePointAverage: Optional[X12R] = element(
        name="ENR08",
        description="Academic Grade Point Average",
        min_length=1,
        max_length=6,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ENR09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="ENR10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="ENR11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="ENR12",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="ENR13",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode4: Optional[X12ID] = element(
        name="ENR14",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier3: Optional[X12ID] = element(
        name="ENR15",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="ENR16",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriodFormatQualifier4: Optional[X12ID] = element(
        name="ENR17",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod4: Optional[X12AN] = element(
        name="ENR18",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode5: Optional[X12ID] = element(
        name="ENR19",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode6: Optional[X12ID] = element(
        name="ENR20",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
