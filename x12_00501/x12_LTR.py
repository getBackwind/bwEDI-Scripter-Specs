# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LTR(Segment):
    """
    LTR - Laboratory Test Results
    
    Description:
        To describe laboratory testing results, normal result ranges, or both
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LTR/
    """
    _id: Literal["LTR"] = id_element(name="LTR")

    CodeListQualifierCode: X12ID = element(
        name="LTR01",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="LTR02",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MeasurementValue: Optional[X12R] = element(
        name="LTR03",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    CodeListQualifierCode2: Optional[X12ID] = element(
        name="LTR05",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="LTR06",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    ShipmentStatusCode: Optional[X12ID] = element(
        name="LTR07",
        description="Shipment Status Code",
        min_length=1,
        max_length=2,
    )

    RangeMinimum: Optional[X12R] = element(
        name="LTR08",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="LTR09",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    GenderCode: Optional[X12ID] = element(
        name="LTR10",
        description="Gender Code",
        min_length=1,
        max_length=1,
    )

    RangeMinimum2: Optional[X12R] = element(
        name="LTR11",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum2: Optional[X12R] = element(
        name="LTR12",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )
