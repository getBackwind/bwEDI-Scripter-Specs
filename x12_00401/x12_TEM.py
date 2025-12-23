# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class TEM(Segment):
    """
    TEM - Pick-up Totals
    
    Description:
        To provide minimal lading data relative to a pick-up
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TEM/
    """
    _id: Literal["TEM"] = id_element(name="TEM")

    Quantity: Optional[X12R] = element(
        name="TEM01",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="TEM02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="TEM03",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="TEM04",
        description="Weight",
        min_length=1,
        max_length=10,
    )
