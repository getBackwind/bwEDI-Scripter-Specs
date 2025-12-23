# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RP(Segment):
    """
    RP - Retirement Product
    
    Description:
        To specify the retirement product characteristics
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RP/
    """
    _id: Literal["RP"] = id_element(name="RP")

    MaintenanceTypeCode: X12ID = element(
        name="RP01",
        description="Maintenance Type Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    InsuranceLineCode: Optional[X12ID] = element(
        name="RP02",
        description="Insurance Line Code",
        min_length=2,
        max_length=3,
    )

    MaintenanceReasonCode: Optional[X12ID] = element(
        name="RP03",
        description="Maintenance Reason Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="RP04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ParticipantStatusCode: Optional[X12ID] = element(
        name="RP05",
        description="Participant Status Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="RP06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    SpecialProcessingType: Optional[X12AN] = element(
        name="RP07",
        description="Special Processing Type",
        min_length=1,
        max_length=6,
    )

    Authority: Optional[X12AN] = element(
        name="RP08",
        description="Authority",
        min_length=1,
        max_length=20,
    )

    PlanCoverageDescription: Optional[X12AN] = element(
        name="RP09",
        description="Plan Coverage Description",
        min_length=1,
        max_length=50,
    )
