# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class AT8(Segment):
    """
    AT8 - Shipment Weight, Packaging and Quantity Data
    
    Description:
        To specify shipment details in terms of weight, and quantity of handling units
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AT8/
    """
    _id: Literal["AT8"] = id_element(name="AT8")

    WeightQualifier: Optional[X12ID] = element(
        name="AT801",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="AT802",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="AT803",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="AT804",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    LadingQuantity2: Optional[X12Nn] = element(
        name="AT805",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="AT806",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="AT807",
        description="Volume",
        min_length=1,
        max_length=8,
    )
