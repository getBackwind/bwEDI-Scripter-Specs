# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class HSD(Segment):
    """
    HSD - Health Care Services Delivery
    
    Description:
        To specify the delivery pattern of health care services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/HSD/
    """
    _id: Literal["HSD"] = id_element(name="HSD")

    QuantityQualifier: Optional[X12ID] = element(
        name="HSD01",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="HSD02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="HSD03",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    SampleSelectionModulus: Optional[X12R] = element(
        name="HSD04",
        description="Sample Selection Modulus",
        min_length=1,
        max_length=6,
    )

    TimePeriodQualifier: Optional[X12ID] = element(
        name="HSD05",
        description="Time Period Qualifier",
        min_length=1,
        max_length=2,
    )

    NumberOfPeriods: Optional[X12Nn] = element(
        name="HSD06",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    ShipDeliveryOrCalendarPatternCode: Optional[X12ID] = element(
        name="HSD07",
        description="Ship/Delivery or Calendar Pattern Code",
        min_length=1,
        max_length=2,
    )

    ShipDeliveryPatternTimeCode: Optional[X12ID] = element(
        name="HSD08",
        description="Ship/Delivery Pattern Time Code",
        min_length=1,
        max_length=1,
    )
