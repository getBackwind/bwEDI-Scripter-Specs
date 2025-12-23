# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class MEA(Segment):
    """
    MEA - Measurements
    
    Description:
        To specify physical measurements or counts, including dimensions, tolerances, variances, and weights
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MEA/
    """
    _id: Literal["MEA"] = id_element(name="MEA")

    MeasurementReferenceIDCode: Optional[X12ID] = element(
        name="MEA01",
        description="Measurement Reference ID Code",
        min_length=2,
        max_length=2,
    )

    MeasurementQualifier: Optional[X12ID] = element(
        name="MEA02",
        description="Measurement Qualifier",
        min_length=1,
        max_length=3,
    )

    MeasurementValue: Optional[X12R] = element(
        name="MEA03",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    RangeMinimum: Optional[X12R] = element(
        name="MEA05",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="MEA06",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    MeasurementSignificanceCode: Optional[X12ID] = element(
        name="MEA07",
        description="Measurement Significance Code",
        min_length=2,
        max_length=2,
    )

    MeasurementAttributeCode: Optional[X12ID] = element(
        name="MEA08",
        description="Measurement Attribute Code",
        min_length=2,
        max_length=2,
    )

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="MEA09",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    MeasurementMethodOrDevice: Optional[X12ID] = element(
        name="MEA10",
        description="Measurement Method or Device",
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="MEA11",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="MEA12",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
