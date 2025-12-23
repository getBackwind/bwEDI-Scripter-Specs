# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SST(Segment):
    """
    SST - Student Academic Status
    
    Description:
        To provide information concerning the student's eligibility to return to the reporting institution, enrollment status, residency for fee purposes, and date and type or status of high school graduation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SST/
    """
    _id: Literal["SST"] = id_element(name="SST")

    StatusReasonCode: Optional[X12ID] = element(
        name="SST01",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="SST02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="SST03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    StatusReasonCode2: Optional[X12ID] = element(
        name="SST04",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="SST05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="SST06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    StatusReasonCode3: Optional[X12ID] = element(
        name="SST07",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="SST08",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SST09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
