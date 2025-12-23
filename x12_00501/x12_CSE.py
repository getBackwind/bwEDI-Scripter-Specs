# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CSE(Segment):
    """
    CSE - Educational Course Information
    
    Description:
        To provide information on an educational course
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CSE/
    """
    _id: Literal["CSE"] = id_element(name="CSE")

    Name: Optional[X12AN] = element(
        name="CSE01",
        description="Name",
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CSE02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    AcademicCreditTypeCode: Optional[X12ID] = element(
        name="CSE03",
        description="Academic Credit Type Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="CSE04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="CSE05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CSE06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    AcademicGradeOrCourseLevelCode: Optional[X12ID] = element(
        name="CSE07",
        description="Academic Grade or Course Level Code",
        min_length=1,
        max_length=2,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="CSE08",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="CSE09",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    EntityTitle: Optional[X12AN] = element(
        name="CSE10",
        description="Entity Title",
        min_length=1,
        max_length=132,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="CSE11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="CSE12",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
