# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn


class SAL(Segment):
    """
    SAL - Salary Information
    
    Description:
        To specify details of commission salary information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SAL/
    """
    _id: Literal["SAL"] = id_element(name="SAL")

    YesNoConditionOrResponseCode: X12ID = element(
        name="SAL01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Amount: Optional[X12Nn] = element(
        name="SAL02",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    LaborRate: Optional[X12Nn] = element(
        name="SAL03",
        description="Labor Rate",
        min_length=3,
        max_length=6,
    )

    NumberOfPeriods: Optional[X12Nn] = element(
        name="SAL04",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="SAL05",
        description="Unit of Time Period or Interval",
    )

    Date: Optional[X12DT] = element(
        name="SAL06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="SAL07",
        description="Date",
        min_length=8,
        max_length=8,
    )
