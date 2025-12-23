# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class BUY(Segment):
    """
    BUY - Loan Buydown
    
    Description:
        To describe the features of a loan buydown
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BUY/
    """
    _id: Literal["BUY"] = id_element(name="BUY")

    LoanBuydownTypeCode: X12ID = element(
        name="BUY01",
        description="Loan Buydown Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    BuydownSourceCode: X12ID = element(
        name="BUY02",
        description="Buydown Source Code",
        mandatory=True,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="BUY03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Percent: Optional[X12R] = element(
        name="BUY04",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Percent2: Optional[X12R] = element(
        name="BUY05",
        description="Percent",
        min_length=1,
        max_length=10,
    )
