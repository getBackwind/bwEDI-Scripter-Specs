# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class AVA(Segment):
    """
    AVA - Funds Availability
    
    Description:
        To indicate the funds availability in days
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AVA/
    """
    _id: Literal["AVA"] = id_element(name="AVA")

    MonetaryAmount: X12R = element(
        name="AVA01",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Availability: X12R = element(
        name="AVA02",
        description="Availability",
        mandatory=True,
        min_length=1,
        max_length=6,
    )
