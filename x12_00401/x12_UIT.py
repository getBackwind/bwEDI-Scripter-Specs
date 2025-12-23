# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class UIT(Segment):
    """
    UIT - Unit Detail
    
    Description:
        To specify item unit data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/UIT/
    """
    _id: Literal["UIT"] = id_element(name="UIT")

    UnitPrice: Optional[X12R] = element(
        name="UIT02",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    BasisOfUnitPriceCode: Optional[X12ID] = element(
        name="UIT03",
        description="Basis of Unit Price Code",
        min_length=2,
        max_length=2,
    )
