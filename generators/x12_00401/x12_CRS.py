# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class CRS(Segment):
    """
    CRS - Course Record
    
    Description:
        To provide the receiving institution or organization with information about courses taken and the status of those courses
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CRS/
    """
    _id: Literal["CRS"] = id_element(name="CRS")

    BasisForAcademicCreditCode: X12ID = element(
        name="CRS01",
        description="Basis for Academic Credit Code",
        mandatory=True,
    )

    AcademicCreditTypeCode: Optional[X12ID] = element(
        name="CRS02",
        description="Academic Credit Type Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="CRS03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="CRS04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    AcademicGradeQualifier: Optional[X12ID] = element(
        name="CRS05",
        description="Academic Grade Qualifier",
        min_length=1,
        max_length=3,
    )

    AcademicGrade: Optional[X12AN] = element(
        name="CRS06",
        description="Academic Grade",
        min_length=1,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CRS07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    AcademicGradeOrCourseLevelCode: Optional[X12ID] = element(
        name="CRS08",
        description="Academic Grade or Course Level Code",
        min_length=1,
        max_length=2,
    )

    CourseRepeatOrNoCountIndicatorCode: Optional[X12ID] = element(
        name="CRS09",
        description="Course Repeat or No Count Indicator Code",
        min_length=1,
        max_length=1,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="CRS10",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="CRS11",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Quantity3: Optional[X12R] = element(
        name="CRS12",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="CRS13",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    Name: Optional[X12AN] = element(
        name="CRS14",
        description="Name",
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CRS15",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Name2: Optional[X12AN] = element(
        name="CRS16",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Quantity4: Optional[X12R] = element(
        name="CRS17",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity5: Optional[X12R] = element(
        name="CRS18",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="CRS19",
        description="Date",
        min_length=8,
        max_length=8,
    )

    OverrideAcademicCourseSourceCode: Optional[X12ID] = element(
        name="CRS20",
        description="Override Academic Course Source Code",
        min_length=2,
        max_length=2,
    )
