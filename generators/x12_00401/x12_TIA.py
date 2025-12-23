# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12R


class TIA(Segment):
    """
    TIA - Tax Information and Amount
    
    Description:
        To specify the tax information and/or amount and to be used for tax information only as established by taxing authorities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TIA/
    """
    _id: Literal["TIA"] = id_element(name="TIA")

    MonetaryAmount: Optional[X12R] = element(
        name="TIA02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    FixedFormatInformation: Optional[X12AN] = element(
        name="TIA03",
        description="Fixed Format Information",
        min_length=1,
        max_length=80,
    )

    Quantity: Optional[X12R] = element(
        name="TIA04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Percent: Optional[X12R] = element(
        name="TIA06",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="TIA07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
