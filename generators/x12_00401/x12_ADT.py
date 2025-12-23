# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn, X12TM


class ADT(Segment):
    """
    ADT - Animal Parturition Status
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ADT/
    """
    _id: Literal["ADT"] = id_element(name="ADT")

    ParturitionStatusCode: X12ID = element(
        name="ADT01",
        description="Parturition Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="ADT02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="ADT03",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="ADT04",
        description="Unit of Time Period or Interval",
    )

    Date2: Optional[X12DT] = element(
        name="ADT05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue2: Optional[X12Nn] = element(
        name="ADT06",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval2: Optional[X12ID] = element(
        name="ADT07",
        description="Unit of Time Period or Interval",
    )

    Time: Optional[X12TM] = element(
        name="ADT08",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TestPeriodOrIntervalValue3: Optional[X12Nn] = element(
        name="ADT09",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval3: Optional[X12ID] = element(
        name="ADT10",
        description="Unit of Time Period or Interval",
    )
