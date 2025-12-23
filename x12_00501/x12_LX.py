# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class LX(Segment):
    """
    LX - Transaction Set Line Number
    
    Description:
        To reference a line number in a transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LX/
    """
    _id: Literal["LX"] = id_element(name="LX")

    AssignedNumber: X12Nn = element(
        name="LX01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )
