# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class F04(Segment):
    """
    F04 - Weight/Volume Loss
    
    Description:
        To report origin and destination weights or volumes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F04/
    """
    _id: Literal["F04"] = id_element(name="F04")

    Weight: Optional[X12R] = element(
        name="F0401",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="F0402",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="F0403",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Weight2: Optional[X12R] = element(
        name="F0404",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode2: Optional[X12ID] = element(
        name="F0405",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    WeightQualifier2: Optional[X12ID] = element(
        name="F0406",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Volume: Optional[X12R] = element(
        name="F0407",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="F0408",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume2: Optional[X12R] = element(
        name="F0409",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier2: Optional[X12ID] = element(
        name="F0410",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )
