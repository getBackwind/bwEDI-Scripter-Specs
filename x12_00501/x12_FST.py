# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class FST(Segment):
    """
    FST - Forecast Schedule
    
    Description:
        To specify the forecasted dates and quantities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FST/
    """
    _id: Literal["FST"] = id_element(name="FST")

    Quantity: X12R = element(
        name="FST01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    ForecastQualifier: X12ID = element(
        name="FST02",
        description="Forecast Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    TimingQualifier: X12ID = element(
        name="FST03",
        description="Timing Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="FST04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="FST05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="FST06",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Time: Optional[X12TM] = element(
        name="FST07",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="FST08",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="FST09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    PlanningScheduleTypeCode: Optional[X12ID] = element(
        name="FST10",
        description="Planning Schedule Type Code",
        min_length=2,
        max_length=2,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="FST11",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    AdjustmentReasonCode: Optional[X12ID] = element(
        name="FST12",
        description="Adjustment Reason Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="FST13",
        description="Description",
        min_length=1,
        max_length=80,
    )
