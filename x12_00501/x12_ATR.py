# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R, X12TM


class ATR(Segment):
    """
    ATR - Animal Test Result
    
    Description:
        To report individual animal test results
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ATR/
    """
    _id: Literal["ATR"] = id_element(name="ATR")

    TestTypeCode: X12ID = element(
        name="ATR01",
        description="Test Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TestPeriodOrIntervalValue: X12Nn = element(
        name="ATR02",
        description="Test Period or Interval Value",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: X12ID = element(
        name="ATR03",
        description="Unit of Time Period or Interval",
        mandatory=True,
    )

    MeasurementValue: Optional[X12R] = element(
        name="ATR04",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    NonNumericTestValue: Optional[X12AN] = element(
        name="ATR06",
        description="Non-Numeric Test Value",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="ATR07",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ATR08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    SurfaceLayerPositionCode: Optional[X12ID] = element(
        name="ATR09",
        description="Surface/Layer/Position Code",
        min_length=2,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="ATR10",
        description="Time",
        min_length=4,
        max_length=8,
    )
