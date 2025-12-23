# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RAP(Segment):
    """
    RAP - Requirement, Attribute, and Proficiency
    
    Description:
        To identify requirements, attributes, and proficiencies of students and/or courses
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RAP/
    """
    _id: Literal["RAP"] = id_element(name="RAP")

    EducationalTestOrRequirementCode: X12ID = element(
        name="RAP01",
        description="Educational Test or Requirement Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    Name: Optional[X12AN] = element(
        name="RAP02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Name2: Optional[X12AN] = element(
        name="RAP03",
        description="Name",
        min_length=1,
        max_length=60,
    )

    UsageIndicator: Optional[X12ID] = element(
        name="RAP04",
        description="Usage Indicator",
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="RAP05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="RAP06",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="RAP07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
