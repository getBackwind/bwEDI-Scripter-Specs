# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class VC1(Segment):
    """
    VC1 - Vehicle Detail
    
    Description:
        To define motor vehicle characteristics
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/VC1/
    """
    _id: Literal["VC1"] = id_element(name="VC1")

    Color: Optional[X12AN] = element(
        name="VC101",
        description="Color",
        min_length=1,
        max_length=10,
    )

    Color2: Optional[X12AN] = element(
        name="VC102",
        description="Color",
        min_length=1,
        max_length=10,
    )

    VehicleDimension: Optional[X12AN] = element(
        name="VC103",
        description="Vehicle Dimension",
        min_length=1,
        max_length=6,
    )

    SpecialHandlingCode: Optional[X12ID] = element(
        name="VC104",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="VC105",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="VC106",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="VC107",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="VC108",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    MeasurementUnitQualifier: Optional[X12ID] = element(
        name="VC109",
        description="Measurement Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Height: Optional[X12R] = element(
        name="VC110",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Length: Optional[X12R] = element(
        name="VC111",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="VC112",
        description="Width",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="VC113",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="VC114",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="VC115",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )
