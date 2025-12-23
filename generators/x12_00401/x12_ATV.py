# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ATV(Segment):
    """
    ATV - Student Activities and Awards
    
    Description:
        To identify the activities in which a student has been involved, awards and honors the student has received, significant achievements, including employment, or publications
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ATV/
    """
    _id: Literal["ATV"] = id_element(name="ATV")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="ATV01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="ATV02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    EntityTitle: Optional[X12AN] = element(
        name="ATV03",
        description="Entity Title",
        min_length=1,
        max_length=132,
    )

    EntityTitle2: Optional[X12AN] = element(
        name="ATV04",
        description="Entity Title",
        min_length=1,
        max_length=132,
    )

    Quantity: Optional[X12R] = element(
        name="ATV05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="ATV07",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ATV08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="ATV09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="ATV10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
