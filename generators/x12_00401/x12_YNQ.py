# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class YNQ(Segment):
    """
    YNQ - Yes/No Question
    
    Description:
        To identify and answer yes and no questions, including the date, time, and comments further qualifying the condition
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/YNQ/
    """
    _id: Literal["YNQ"] = id_element(name="YNQ")

    ConditionIndicator: Optional[X12ID] = element(
        name="YNQ01",
        description="Condition Indicator",
    )

    YesNoValue: X12ID = element(
        name="YNQ02",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="YNQ03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="YNQ04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="YNQ05",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    FreeFormMessageText2: Optional[X12AN] = element(
        name="YNQ06",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    FreeFormMessageText3: Optional[X12AN] = element(
        name="YNQ07",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="YNQ08",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="YNQ09",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    FreeFormMessageText4: Optional[X12AN] = element(
        name="YNQ10",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )
