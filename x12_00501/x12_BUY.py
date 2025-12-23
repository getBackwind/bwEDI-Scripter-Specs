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
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BUY/
    """
    _id: Literal["BUY"] = id_element(name="BUY")

    LoanBuydownTypeCode: X12ID = element(
        name="BUY01",
        description="Loan Buydown Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    SourceOfFundsCode: X12ID = element(
        name="BUY02",
        description="Source of Funds Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="BUY03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="BUY04",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    PercentageAsDecimal2: Optional[X12R] = element(
        name="BUY05",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
