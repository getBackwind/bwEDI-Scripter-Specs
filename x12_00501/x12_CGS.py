# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn


class CGS(Segment):
    """
    CGS - Charge
    
    Description:
        To specify charges
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CGS/
    """
    _id: Literal["CGS"] = id_element(name="CGS")

    AmountCharged: Optional[X12Nn] = element(
        name="CGS01",
        description="Amount Charged",
        min_length=1,
        max_length=15,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="CGS02",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="CGS03",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="CGS04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    SpecialChargeOrAllowanceCode: Optional[X12ID] = element(
        name="CGS05",
        description="Special Charge or Allowance Code",
        min_length=3,
        max_length=3,
    )
