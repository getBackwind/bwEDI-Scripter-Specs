# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ISI(Segment):
    """
    ISI - Institutional Staff Information
    
    Description:
        To provide information about number and type of staff in an institution
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ISI/
    """
    _id: Literal["ISI"] = id_element(name="ISI")

    CodeListQualifierCode: X12ID = element(
        name="ISI01",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="ISI02",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="ISI03",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="ISI05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ISI06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
