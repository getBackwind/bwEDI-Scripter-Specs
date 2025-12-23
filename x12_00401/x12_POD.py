# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12TM


class POD(Segment):
    """
    POD - Proof of Delivery
    
    Description:
        To provide proof of delivery
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/POD/
    """
    _id: Literal["POD"] = id_element(name="POD")

    Date: X12DT = element(
        name="POD01",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="POD02",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Name: X12AN = element(
        name="POD03",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )
