# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class INT(Segment):
    """
    INT - Interest
    
    Description:
        To specify interest rate and type and the applicable time period
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/INT/
    """
    _id: Literal["INT"] = id_element(name="INT")

    InterestTypeCode: X12ID = element(
        name="INT01",
        description="Interest Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    InterestRate: Optional[X12R] = element(
        name="INT02",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="INT03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="INT04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Quantity: Optional[X12R] = element(
        name="INT05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
