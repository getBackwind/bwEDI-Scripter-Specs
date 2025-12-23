# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class AT9(Segment):
    """
    AT9 - Trailer or Container Dimension and Weight
    
    Description:
        To specify trailer or container dimensions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AT9/
    """
    _id: Literal["AT9"] = id_element(name="AT9")

    EquipmentLength: Optional[X12Nn] = element(
        name="AT901",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    Height: Optional[X12R] = element(
        name="AT902",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="AT903",
        description="Width",
        min_length=1,
        max_length=8,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="AT904",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="AT905",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="AT906",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="AT907",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="AT908",
        description="Volume",
        min_length=1,
        max_length=8,
    )
