# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R, X12TM


class ESI(Segment):
    """
    ESI - Employment Status Information
    
    Description:
        To specify status of employment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ESI/
    """
    _id: Literal["ESI"] = id_element(name="ESI")

    YesNoConditionOrResponseCode: X12ID = element(
        name="ESI01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="ESI02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="ESI03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Time: Optional[X12TM] = element(
        name="ESI04",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Quantity: Optional[X12R] = element(
        name="ESI05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    EmploymentStatusCode: Optional[X12ID] = element(
        name="ESI06",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    WorkIntensityCode: Optional[X12ID] = element(
        name="ESI07",
        description="Work Intensity Code",
        min_length=1,
        max_length=1,
    )

    ReasonStoppedWorkCode: Optional[X12ID] = element(
        name="ESI08",
        description="Reason Stopped Work Code",
        min_length=2,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="ESI09",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )
