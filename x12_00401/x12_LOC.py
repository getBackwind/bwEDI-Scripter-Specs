# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LOC(Segment):
    """
    LOC - Location
    
    Description:
        To describe the location in space and time of the axis of an item relative to an origin axis Euclidean geometry has been assumed with orthogonal axes; the sequence of axes has been chosen in the customary sequence of X, Y, and Z, however, it is possible to just use two-dimensional space rather than three-dimensional space
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LOC/
    """
    _id: Literal["LOC"] = id_element(name="LOC")

    ReferenceIdentificationQualifier: X12ID = element(
        name="LOC01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="LOC02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="LOC03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="LOC04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Category: Optional[X12AN] = element(
        name="LOC05",
        description="Category",
        min_length=1,
        max_length=6,
    )

    ReferenceIdentificationQualifier2: Optional[X12ID] = element(
        name="LOC06",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="LOC07",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description2: Optional[X12AN] = element(
        name="LOC08",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ReferenceIdentification4: Optional[X12AN] = element(
        name="LOC09",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    MeasurementValue: Optional[X12R] = element(
        name="LOC10",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    MeasurementValue2: Optional[X12R] = element(
        name="LOC12",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    MeasurementValue3: Optional[X12R] = element(
        name="LOC14",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    MeasurementValue4: Optional[X12R] = element(
        name="LOC16",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    MeasurementValue5: Optional[X12R] = element(
        name="LOC18",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    MeasurementValue6: Optional[X12R] = element(
        name="LOC20",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    ReferenceIdentificationQualifier3: Optional[X12ID] = element(
        name="LOC22",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification5: Optional[X12AN] = element(
        name="LOC23",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description3: Optional[X12AN] = element(
        name="LOC24",
        description="Description",
        min_length=1,
        max_length=80,
    )
