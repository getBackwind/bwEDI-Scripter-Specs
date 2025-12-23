# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class QTY(Segment):
    """
    QTY - Quantity
    
    Description:
        To specify quantity information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/QTY/
    """
    _id: Literal["QTY"] = id_element(name="QTY")

    QuantityQualifier: X12ID = element(
        name="QTY01",
        description="Quantity Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="QTY02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="QTY04",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )
