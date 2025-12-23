# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class HLH(Segment):
    """
    HLH - Health Information
    
    Description:
        To provide health information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/HLH/
    """
    _id: Literal["HLH"] = id_element(name="HLH")

    HealthRelatedCode: Optional[X12ID] = element(
        name="HLH01",
        description="Health-Related Code",
        min_length=1,
        max_length=1,
    )

    Height: Optional[X12R] = element(
        name="HLH02",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Weight: Optional[X12R] = element(
        name="HLH03",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight2: Optional[X12R] = element(
        name="HLH04",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Description: Optional[X12AN] = element(
        name="HLH05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    CurrentHealthConditionCode: Optional[X12ID] = element(
        name="HLH06",
        description="Current Health Condition Code",
        min_length=1,
        max_length=1,
    )

    Description2: Optional[X12AN] = element(
        name="HLH07",
        description="Description",
        min_length=1,
        max_length=80,
    )
