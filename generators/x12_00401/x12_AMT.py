# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class AMT(Segment):
    """
    AMT - Monetary Amount
    
    Description:
        To indicate the total monetary amount
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AMT/
    """
    _id: Literal["AMT"] = id_element(name="AMT")

    AmountQualifier: X12ID = element(
        name="AMT01",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    TotalAmount: X12R = element(
        name="AMT02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    CreditDebitFlagCode: Optional[X12ID] = element(
        name="AMT03",
        description="Credit/Debit Flag Code",
        min_length=1,
        max_length=1,
    )
