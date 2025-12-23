# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class C4(Segment):
    """
    C4 - Alternate Amount Due
    
    Description:
        To specify alternate payment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/C4/
    """
    _id: Literal["C4"] = id_element(name="C4")

    CurrencyCode: X12ID = element(
        name="C401",
        description="Currency Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    NetAmountDue: X12Nn = element(
        name="C402",
        description="Net Amount Due",
        mandatory=True,
        min_length=1,
        max_length=12,
    )
