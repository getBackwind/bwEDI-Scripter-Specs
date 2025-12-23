# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class ANI(Segment):
    """
    ANI - Animal Identification
    
    Description:
        To uniquely identify each animal within the group
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ANI/
    """
    _id: Literal["ANI"] = id_element(name="ANI")

    ReferenceIdentification: X12AN = element(
        name="ANI01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="ANI02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="ANI03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="ANI04",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="ANI05",
        description="Unit of Time Period or Interval",
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="ANI06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="ANI07",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date3: Optional[X12DT] = element(
        name="ANI08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification4: Optional[X12AN] = element(
        name="ANI09",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
