# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R, X12TM


class JIT(Segment):
    """
    JIT - Just-In-Time Schedule
    
    Description:
        To identify the specific shipping/delivery time in terms of a 24-hour clock and identify the associated quantity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/JIT/
    """
    _id: Literal["JIT"] = id_element(name="JIT")

    Quantity: X12R = element(
        name="JIT01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Time: X12TM = element(
        name="JIT02",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )
