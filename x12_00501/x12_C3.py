# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class C3(Segment):
    """
    C3 - Currency Identifier
    
    Description:
        To specify the currency being used in the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/C3/
    """
    _id: Literal["C3"] = id_element(name="C3")

    CurrencyCode: X12ID = element(
        name="C301",
        description="Currency Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    ExchangeRate: Optional[X12R] = element(
        name="C302",
        description="Exchange Rate",
        min_length=4,
        max_length=10,
    )

    CurrencyCode2: Optional[X12ID] = element(
        name="C303",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    CurrencyCode3: Optional[X12ID] = element(
        name="C304",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
