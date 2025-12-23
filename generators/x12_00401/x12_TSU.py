# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R, X12TM


class TSU(Segment):
    """
    TSU - Transaction Summary
    
    Description:
        To provide specific transaction summary information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TSU/
    """
    _id: Literal["TSU"] = id_element(name="TSU")

    CodeListQualifierCode: X12ID = element(
        name="TSU01",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="TSU02",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    MonetaryAmount: X12R = element(
        name="TSU03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="TSU04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="TSU05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="TSU06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="TSU07",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="TSU08",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
