# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class GDP(Segment):
    """
    GDP - General Dosing Parameters
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/GDP/
    """
    _id: Literal["GDP"] = id_element(name="GDP")

    MeasurementValue: X12R = element(
        name="GDP01",
        description="Measurement Value",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    RouteOfAdministration: Optional[X12AN] = element(
        name="GDP03",
        description="Route of Administration",
        min_length=1,
        max_length=20,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="GDP04",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="GDP05",
        description="Unit of Time Period or Interval",
    )

    TestPeriodOrIntervalValue2: Optional[X12Nn] = element(
        name="GDP06",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval2: Optional[X12ID] = element(
        name="GDP07",
        description="Unit of Time Period or Interval",
    )
