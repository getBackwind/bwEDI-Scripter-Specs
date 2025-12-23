# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class AWD(Segment):
    """
    AWD - Amount with Description
    
    Description:
        To specify a code and/or description with an associated amount
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AWD/
    """
    _id: Literal["AWD"] = id_element(name="AWD")

    MonetaryAmount: Optional[X12R] = element(
        name="AWD02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="AWD03",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="AWD04",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
