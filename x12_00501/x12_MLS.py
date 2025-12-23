# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MLS(Segment):
    """
    MLS - Milestone
    
    Description:
        To identify milestone details for tasks or activities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MLS/
    """
    _id: Literal["MLS"] = id_element(name="MLS")

    MilestoneNumberIdentification: X12AN = element(
        name="MLS01",
        description="Milestone Number Identification",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    Description: Optional[X12AN] = element(
        name="MLS02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    WorkStatusCode: Optional[X12ID] = element(
        name="MLS03",
        description="Work Status Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="MLS04",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
