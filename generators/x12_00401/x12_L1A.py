# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class L1A(Segment):
    """
    L1A - Billing Identification
    
    Description:
        To identify the road issuing the freight bill and the amount for which the freight bill was issued
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/L1A/
    """
    _id: Literal["L1A"] = id_element(name="L1A")

    Amount: Optional[X12Nn] = element(
        name="L1A01",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="L1A02",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
