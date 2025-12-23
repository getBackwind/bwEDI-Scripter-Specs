# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn


class AOC(Segment):
    """
    AOC - Animal Offspring Counts
    
    Description:
        To report offspring counts for the parent animal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AOC/
    """
    _id: Literal["AOC"] = id_element(name="AOC")

    OffspringCountCode: X12ID = element(
        name="AOC01",
        description="Offspring Count Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Count: X12Nn = element(
        name="AOC02",
        description="Count",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    Date: Optional[X12DT] = element(
        name="AOC03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="AOC04",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="AOC05",
        description="Unit of Time Period or Interval",
    )
