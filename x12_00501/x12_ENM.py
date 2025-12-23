# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ENM(Segment):
    """
    ENM - School Enrollment Data
    
    Description:
        To specify education enrollment information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ENM/
    """
    _id: Literal["ENM"] = id_element(name="ENM")

    StatusReasonCode: X12ID = element(
        name="ENM01",
        description="Status Reason Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="ENM02",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    SessionCode: Optional[X12ID] = element(
        name="ENM03",
        description="Session Code",
        min_length=1,
        max_length=1,
    )

    GenderCode: Optional[X12ID] = element(
        name="ENM05",
        description="Gender Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="ENM06",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="ENM07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ENM08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
