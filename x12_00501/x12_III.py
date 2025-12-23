# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class III(Segment):
    """
    III - Information
    
    Description:
        To report information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/III/
    """
    _id: Literal["III"] = id_element(name="III")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="III01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="III02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    CodeCategory: Optional[X12ID] = element(
        name="III03",
        description="Code Category",
        min_length=2,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="III04",
        description="Free-form Message Text",
        min_length=1,
        max_length=264,
    )

    Quantity: Optional[X12R] = element(
        name="III05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="III07",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    SurfaceLayerPositionCode2: Optional[X12ID] = element(
        name="III08",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    SurfaceLayerPositionCode3: Optional[X12ID] = element(
        name="III09",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )
