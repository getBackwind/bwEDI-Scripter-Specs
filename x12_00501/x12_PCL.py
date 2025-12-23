# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PCL(Segment):
    """
    PCL - Previous College
    
    Description:
        To provide the receiving educational institution or agency with information concerning the student's previous postsecondary education experience
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PCL/
    """
    _id: Literal["PCL"] = id_element(name="PCL")

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="PCL01",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="PCL02",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PCL03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PCL04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    AcademicDegreeCode: Optional[X12ID] = element(
        name="PCL05",
        description="Academic Degree Code",
        min_length=3,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="PCL06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Description: Optional[X12AN] = element(
        name="PCL07",
        description="Description",
        min_length=1,
        max_length=80,
    )
