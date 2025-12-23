# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class STA(Segment):
    """
    STA - Statistics
    
    Description:
        To provide summary statistics related to a specific collection of test result values
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/STA/
    """
    _id: Literal["STA"] = id_element(name="STA")

    StatisticCode: X12ID = element(
        name="STA01",
        description="Statistic Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MeasurementValue: X12R = element(
        name="STA02",
        description="Measurement Value",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    MeasurementQualifier: Optional[X12ID] = element(
        name="STA04",
        description="Measurement Qualifier",
        min_length=1,
        max_length=3,
    )

    MeasurementReferenceIDCode: Optional[X12ID] = element(
        name="STA05",
        description="Measurement Reference ID Code",
        min_length=2,
        max_length=2,
    )

    RangeMinimum: Optional[X12R] = element(
        name="STA06",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="STA07",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    MeasurementSignificanceCode: Optional[X12ID] = element(
        name="STA08",
        description="Measurement Significance Code",
        min_length=2,
        max_length=2,
    )
