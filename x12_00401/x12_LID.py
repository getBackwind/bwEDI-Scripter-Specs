# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LID(Segment):
    """
    LID - Loss Information Description
    
    Description:
        To provide details on a specific insurance claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LID/
    """
    _id: Literal["LID"] = id_element(name="LID")

    DateTimePeriodFormatQualifier: X12ID = element(
        name="LID01",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="LID02",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )

    IndustryCode: Optional[X12AN] = element(
        name="LID03",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="LID04",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="LID05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LID06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="LID07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Description2: Optional[X12AN] = element(
        name="LID08",
        description="Description",
        min_length=1,
        max_length=80,
    )
