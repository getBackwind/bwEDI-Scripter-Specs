# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class LET(Segment):
    """
    LET - Load and Equipment Type
    
    Description:
        To identify the load and equipment type for a high/wide shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LET/
    """
    _id: Literal["LET"] = id_element(name="LET")

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="LET01",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="LET02",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    ShapeCode: Optional[X12ID] = element(
        name="LET03",
        description="Shape Code",
        min_length=2,
        max_length=2,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="LET04",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )
