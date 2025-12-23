# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class DEG(Segment):
    """
    DEG - Degree Record
    
    Description:
        To provide information about an educational institution's academic award
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DEG/
    """
    _id: Literal["DEG"] = id_element(name="DEG")

    AcademicDegreeCode: X12ID = element(
        name="DEG01",
        description="Academic Degree Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="DEG02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="DEG03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Description: Optional[X12AN] = element(
        name="DEG04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="DEG05",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
