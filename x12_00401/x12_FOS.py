# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class FOS(Segment):
    """
    FOS - Field of Study
    
    Description:
        To provide the receiving institution or agency with information about a course or field of study associated with an academic program
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FOS/
    """
    _id: Literal["FOS"] = id_element(name="FOS")

    AcademicFieldOfStudyLevelOrTypeCode: X12ID = element(
        name="FOS01",
        description="Academic Field of Study Level or Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="FOS02",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="FOS03",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Description: Optional[X12AN] = element(
        name="FOS04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="FOS05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity: Optional[X12R] = element(
        name="FOS06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="FOS07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
