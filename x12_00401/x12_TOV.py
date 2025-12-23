# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TOV(Segment):
    """
    TOV - Vehicle Use Information
    
    Description:
        To report usage of a vehicle
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TOV/
    """
    _id: Literal["TOV"] = id_element(name="TOV")

    HazardousVehicleTypeCode: X12ID = element(
        name="TOV01",
        description="Hazardous Vehicle Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="TOV02",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="TOV03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="TOV04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="TOV05",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="TOV06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
