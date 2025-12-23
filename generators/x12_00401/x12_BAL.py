# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class BAL(Segment):
    """
    BAL - Balance Detail
    
    Description:
        To identify the specific monetary balances associated with a particular account
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BAL/
    """
    _id: Literal["BAL"] = id_element(name="BAL")

    BalanceTypeCode: X12ID = element(
        name="BAL01",
        description="Balance Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    AmountQualifierCode: X12ID = element(
        name="BAL02",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="BAL03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )
