# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class TBA(Segment):
    """
    TBA - Temporary Buydown Adjustment
    
    Description:
        To indicate amount or period of temporary buydown adjustment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TBA/
    """
    _id: Literal["TBA"] = id_element(name="TBA")

    Quantity: Optional[X12R] = element(
        name="TBA02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Percent: Optional[X12R] = element(
        name="TBA03",
        description="Percent",
        min_length=1,
        max_length=10,
    )
