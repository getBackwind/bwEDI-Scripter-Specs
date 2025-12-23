# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class PYM(Segment):
    """
    PYM - Payment Manner and Percentage
    
    Description:
        To specify manner in which bills are paid either to a specific vendor or overall to all vendors
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PYM/
    """
    _id: Literal["PYM"] = id_element(name="PYM")

    RatingCode: Optional[X12ID] = element(
        name="PYM01",
        description="Rating Code",
        min_length=2,
        max_length=2,
    )

    UnitOfTimePeriodOrInterval: Optional[X12ID] = element(
        name="PYM02",
        description="Unit of Time Period or Interval",
    )

    NumberOfPeriods: Optional[X12Nn] = element(
        name="PYM03",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    NumberOfPeriods2: Optional[X12Nn] = element(
        name="PYM04",
        description="Number of Periods",
        min_length=1,
        max_length=3,
    )

    TimePeriodQualifier: Optional[X12ID] = element(
        name="PYM05",
        description="Time Period Qualifier",
        min_length=1,
        max_length=2,
    )

    RatingRemarksCode: Optional[X12ID] = element(
        name="PYM06",
        description="Rating Remarks Code",
        min_length=2,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="PYM07",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
