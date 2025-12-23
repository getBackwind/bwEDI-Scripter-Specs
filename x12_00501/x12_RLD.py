# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class RLD(Segment):
    """
    RLD - Down Payment Data
    
    Description:
        To provide amount or nature of loan down payment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RLD/
    """
    _id: Literal["RLD"] = id_element(name="RLD")

    TypeOfFundsCode: Optional[X12ID] = element(
        name="RLD01",
        description="Type of Funds Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="RLD02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Description: Optional[X12AN] = element(
        name="RLD03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="RLD04",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )
