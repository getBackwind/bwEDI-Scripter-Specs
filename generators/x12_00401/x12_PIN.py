# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class PIN(Segment):
    """
    PIN - Previous Incident
    
    Description:
        To identify details of previous insurance losses
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PIN/
    """
    _id: Literal["PIN"] = id_element(name="PIN")

    AssignedNumber: X12Nn = element(
        name="PIN01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PIN02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PIN03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Name: Optional[X12AN] = element(
        name="PIN04",
        description="Name",
        min_length=1,
        max_length=60,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="PIN05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="PIN06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    IndustryCode: Optional[X12AN] = element(
        name="PIN07",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
