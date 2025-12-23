# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class OQS(Segment):
    """
    OQS - Order Quantity Sequence
    
    Description:
        To specify number assigned to a unit within a multiple unit order
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/OQS/
    """
    _id: Literal["OQS"] = id_element(name="OQS")

    SequenceValue: X12R = element(
        name="OQS01",
        description="Sequence Value",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    QuantityOrdered: X12R = element(
        name="OQS02",
        description="Quantity Ordered",
        mandatory=True,
        min_length=1,
        max_length=15,
    )
