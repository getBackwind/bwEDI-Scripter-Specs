# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class AST(Segment):
    """
    AST - Animal Reproductive Status
    
    Description:
        To report reproductive status for the parent animal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AST/
    """
    _id: Literal["AST"] = id_element(name="AST")

    YesNoConditionOrResponseCode: X12ID = element(
        name="AST01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="AST02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="AST03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue: Optional[X12Nn] = element(
        name="AST04",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="AST05",
        description="Unit of Time Period or Interval",
    )

    Date2: Optional[X12DT] = element(
        name="AST06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue2: Optional[X12Nn] = element(
        name="AST07",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval2: Optional[X12ID] = element(
        name="AST08",
        description="Unit of Time Period or Interval",
    )

    Date3: Optional[X12DT] = element(
        name="AST09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TestPeriodOrIntervalValue3: Optional[X12Nn] = element(
        name="AST10",
        description="Test Period or Interval Value",
        min_length=1,
        max_length=6,
    )

    UnitOfTimePeriodOrInterval3: Optional[X12ID] = element(
        name="AST11",
        description="Unit of Time Period or Interval",
    )
