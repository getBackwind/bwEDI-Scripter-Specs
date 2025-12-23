# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PDE(Segment):
    """
    PDE - Property Metes and Bounds Description
    
    Description:
        To describe real estate property by boundary lines with their terminal points and angles; this segment defines legal boundaries of real estate property
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PDE/
    """
    _id: Literal["PDE"] = id_element(name="PDE")

    FreeFormMessageText: Optional[X12AN] = element(
        name="PDE01",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    DirectionIdentifierCode: Optional[X12ID] = element(
        name="PDE02",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )

    MeasurementValue: Optional[X12R] = element(
        name="PDE04",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )
