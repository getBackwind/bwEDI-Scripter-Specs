# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class WLD(Segment):
    """
    WLD - Workload Detail
    
    Description:
        To provide information on a workload task
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/WLD/
    """
    _id: Literal["WLD"] = id_element(name="WLD")

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="WLD01",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="WLD02",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    AcademicGradeOrCourseLevelCode: Optional[X12ID] = element(
        name="WLD03",
        description="Academic Grade or Course Level Code",
        min_length=1,
        max_length=2,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="WLD04",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    Count: Optional[X12Nn] = element(
        name="WLD05",
        description="Count",
        min_length=1,
        max_length=9,
    )

    DayRotation: Optional[X12AN] = element(
        name="WLD06",
        description="Day Rotation",
        min_length=1,
        max_length=7,
    )

    Count2: Optional[X12Nn] = element(
        name="WLD07",
        description="Count",
        min_length=1,
        max_length=9,
    )

    Name: Optional[X12AN] = element(
        name="WLD08",
        description="Name",
        min_length=1,
        max_length=60,
    )

    InstructionalSettingCode: Optional[X12ID] = element(
        name="WLD09",
        description="Instructional Setting Code",
        min_length=1,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="WLD10",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
