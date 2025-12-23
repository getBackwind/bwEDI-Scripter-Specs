# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class FAC(Segment):
    """
    FAC - Facing Direction
    
    Description:
        To identify the direction the equipment is facing
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FAC/
    """
    _id: Literal["FAC"] = id_element(name="FAC")

    EquipmentInitial: X12AN = element(
        name="FAC01",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="FAC02",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="FAC03",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    DirectionFacing: Optional[X12ID] = element(
        name="FAC04",
        description="Direction Facing",
    )

    EquipmentStatusCode: Optional[X12ID] = element(
        name="FAC05",
        description="Equipment Status Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="FAC06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
