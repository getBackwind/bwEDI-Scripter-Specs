# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SES(Segment):
    """
    SES - Academic Session Header
    
    Description:
        To identify the particular academic session in which the activity which follows took place
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SES/
    """
    _id: Literal["SES"] = id_element(name="SES")

    DateTimePeriod: X12AN = element(
        name="SES01",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    Count: Optional[X12Nn] = element(
        name="SES02",
        description="Count",
        min_length=1,
        max_length=9,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="SES03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    SessionCode: Optional[X12ID] = element(
        name="SES04",
        description="Session Code",
        min_length=1,
        max_length=1,
    )

    Name: Optional[X12AN] = element(
        name="SES05",
        description="Name",
        min_length=1,
        max_length=60,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="SES06",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="SES07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="SES08",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod4: Optional[X12AN] = element(
        name="SES09",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="SES10",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="SES11",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="SES12",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Name2: Optional[X12AN] = element(
        name="SES13",
        description="Name",
        min_length=1,
        max_length=60,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="SES14",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
