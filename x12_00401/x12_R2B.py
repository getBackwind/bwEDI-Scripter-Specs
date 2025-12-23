# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class R2B(Segment):
    """
    R2B - Junctions and Proportions
    
    Description:
        To identify routing and proportion detail for carriers participating in the route
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/R2B/
    """
    _id: Literal["R2B"] = id_element(name="R2B")

    StandardCarrierAlphaCode: X12ID = element(
        name="R2B01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Rule260JunctionCode: Optional[X12ID] = element(
        name="R2B02",
        description="Rule 260 Junction Code",
        min_length=1,
        max_length=5,
    )

    Amount: Optional[X12Nn] = element(
        name="R2B03",
        description="Amount",
        min_length=1,
        max_length=15,
    )
