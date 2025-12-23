# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LCT(Segment):
    """
    LCT - Logistics Container Tracking Information
    
    Description:
        To identify the necessary information for tracking containers and identifying contents of containers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LCT/
    """
    _id: Literal["LCT"] = id_element(name="LCT")

    ReferenceIdentification: X12AN = element(
        name="LCT01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    PackagingFormCode: X12ID = element(
        name="LCT02",
        description="Packaging Form Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="LCT03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="LCT04",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    UnitWeight: Optional[X12R] = element(
        name="LCT05",
        description="Unit Weight",
        min_length=1,
        max_length=8,
    )

    MeasurementUnitQualifier: Optional[X12ID] = element(
        name="LCT06",
        description="Measurement Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Length: Optional[X12R] = element(
        name="LCT07",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="LCT08",
        description="Width",
        min_length=1,
        max_length=8,
    )

    Height: Optional[X12R] = element(
        name="LCT09",
        description="Height",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="LCT10",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="LCT11",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    PalletExchangeCode: Optional[X12ID] = element(
        name="LCT12",
        description="Pallet Exchange Code",
        min_length=1,
        max_length=1,
    )
