# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class INV(Segment):
    """
    INV - Investment Vehicle Selection
    
    Description:
        To specify type of investment vehicle or account and other basic data about the investment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/INV/
    """
    _id: Literal["INV"] = id_element(name="INV")

    Description: X12AN = element(
        name="INV01",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )

    Percent: Optional[X12R] = element(
        name="INV02",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="INV03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="INV04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="INV05",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    Description2: Optional[X12AN] = element(
        name="INV06",
        description="Description",
        min_length=1,
        max_length=80,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="INV07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
