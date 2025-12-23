# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MKS(Segment):
    """
    MKS - Marks Awarded
    
    Description:
        To provide additional information to the receiving institution about the marks, or series of marks, a student was awarded in a particular course
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MKS/
    """
    _id: Literal["MKS"] = id_element(name="MKS")

    MarkCodeType: Optional[X12ID] = element(
        name="MKS01",
        description="Mark Code Type",
        min_length=1,
        max_length=2,
    )

    AcademicGradeQualifier: Optional[X12ID] = element(
        name="MKS02",
        description="Academic Grade Qualifier",
        min_length=1,
        max_length=3,
    )

    AcademicGrade: Optional[X12AN] = element(
        name="MKS03",
        description="Academic Grade",
        min_length=1,
        max_length=3,
    )
