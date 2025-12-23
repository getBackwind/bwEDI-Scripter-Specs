# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn


class ADI(Segment):
    """
    ADI - Animal Disposition
    
    Description:
        To record the disposition of an individual animal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ADI/
    """
    _id: Literal["ADI"] = id_element(name="ADI")

    AnimalDispositionCode: X12ID = element(
        name="ADI01",
        description="Animal Disposition Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="ADI02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="ADI03",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="ADI04",
        description="Unit of Time Period or Interval",
    )
