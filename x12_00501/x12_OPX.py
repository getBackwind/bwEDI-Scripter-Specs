# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class OPX(Segment):
    """
    OPX - Placement Criteria
    
    Description:
        To provide receiving educational institution or agency with information concerning the placement criteria or status of the student in a program
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/OPX/
    """
    _id: Literal["OPX"] = id_element(name="OPX")

    YesNoConditionOrResponseCode: X12ID = element(
        name="OPX01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PlacementCriteriaCode: Optional[X12ID] = element(
        name="OPX02",
        description="Placement Criteria Code",
        min_length=1,
        max_length=1,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="OPX03",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    EducationalTestOrRequirementCode: Optional[X12ID] = element(
        name="OPX04",
        description="Educational Test or Requirement Code",
        min_length=1,
        max_length=3,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="OPX05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
