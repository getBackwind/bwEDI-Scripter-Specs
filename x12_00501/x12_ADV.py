# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class ADV(Segment):
    """
    ADV - Advertising Demographic Information
    
    Description:
        To convey advertising demographic information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ADV/
    """
    _id: Literal["ADV"] = id_element(name="ADV")

    AgencyQualifierCode: X12ID = element(
        name="ADV01",
        description="Agency Qualifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ServiceCharacteristicsQualifier: X12AN = element(
        name="ADV02",
        description="Service Characteristics Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    RangeMinimum: Optional[X12R] = element(
        name="ADV03",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="ADV04",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    Category: Optional[X12AN] = element(
        name="ADV05",
        description="Category",
        min_length=1,
        max_length=6,
    )

    ServiceCharacteristicsQualifier2: Optional[X12AN] = element(
        name="ADV06",
        description="Service Characteristics Qualifier",
        min_length=2,
        max_length=3,
    )

    MeasurementValue: Optional[X12R] = element(
        name="ADV07",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )
