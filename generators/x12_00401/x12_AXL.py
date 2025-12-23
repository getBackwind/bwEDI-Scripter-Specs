# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class AXL(Segment):
    """
    AXL - Vehicle Axle Measurements
    
    Description:
        To specify axle measurements for loading vehicles on aircraft or other conveyances
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AXL/
    """
    _id: Literal["AXL"] = id_element(name="AXL")

    ProductServiceIDQualifier: X12ID = element(
        name="AXL01",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="AXL02",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    MeasurementUnitQualifier: Optional[X12ID] = element(
        name="AXL03",
        description="Measurement Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Length: Optional[X12R] = element(
        name="AXL04",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="AXL05",
        description="Width",
        min_length=1,
        max_length=8,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="AXL06",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="AXL07",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="AXL08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
