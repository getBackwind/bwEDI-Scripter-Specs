# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn, X12R


class W14(Segment):
    """
    W14 - Total Receipt Information
    
    Description:
        To indicate total received quantity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W14/
    """
    _id: Literal["W14"] = id_element(name="W14")

    QuantityReceived: X12R = element(
        name="W1401",
        description="Quantity Received",
        mandatory=True,
        min_length=1,
        max_length=7,
    )

    NumberOfUnitsShipped: Optional[X12R] = element(
        name="W1402",
        description="Number of Units Shipped",
        min_length=1,
        max_length=10,
    )

    QuantityDamagedOnHold: Optional[X12R] = element(
        name="W1403",
        description="Quantity Damaged/On Hold",
        min_length=1,
        max_length=9,
    )

    LadingQuantityReceived: Optional[X12Nn] = element(
        name="W1404",
        description="Lading Quantity Received",
        min_length=1,
        max_length=7,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="W1405",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )
