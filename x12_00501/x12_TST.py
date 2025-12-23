# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TST(Segment):
    """
    TST - Test Score Record
    
    Description:
        To provide information about national, regional, state, or local tests that a student has taken
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TST/
    """
    _id: Literal["TST"] = id_element(name="TST")

    EducationalTestOrRequirementCode: X12ID = element(
        name="TST01",
        description="Educational Test or Requirement Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    Name: Optional[X12AN] = element(
        name="TST02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="TST03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="TST04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="TST05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="TST06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="TST07",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    LevelOfIndividualTestOrCourseCode2: Optional[X12ID] = element(
        name="TST08",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="TST09",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    TestNormTypeCode: Optional[X12ID] = element(
        name="TST10",
        description="Test Norm Type Code",
        min_length=1,
        max_length=1,
    )

    TestNormingPeriodCode: Optional[X12ID] = element(
        name="TST11",
        description="Test Norming Period Code",
        min_length=1,
        max_length=1,
    )

    LanguageCode: Optional[X12ID] = element(
        name="TST12",
        description="Language Code",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="TST13",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="TST14",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="TST15",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    TestScoreInterpretationCode: Optional[X12ID] = element(
        name="TST16",
        description="Test Score Interpretation Code",
        min_length=1,
        max_length=1,
    )

    AcademicSummarySource: Optional[X12ID] = element(
        name="TST17",
        description="Academic Summary Source",
    )
