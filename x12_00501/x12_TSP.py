# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class TSP(Segment):
    """
    TSP - Test Period or Interval
    
    Description:
        To describe a specific period or interval at which tests are performed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TSP/
    """
    _id: Literal["TSP"] = id_element(name="TSP")

    TestPeriodOrIntervalQualifier: X12ID = element(
        name="TSP01",
        description="Test Period or Interval Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="TSP02",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="TSP03",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="TSP04",
        description="Unit of Time Period or Interval",
    )
