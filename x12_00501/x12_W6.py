# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class W6(Segment):
    """
    W6 - Special Handling Information
    
    Description:
        To provide special handling information that may be necessary for safe handling of shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W6/
    """
    _id: Literal["W6"] = id_element(name="W6")

    SpecialHandlingCode: X12ID = element(
        name="W601",
        description="Special Handling Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    SpecialHandlingCode2: Optional[X12ID] = element(
        name="W602",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    SpecialHandlingCode3: Optional[X12ID] = element(
        name="W603",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    SpecialHandlingCode4: Optional[X12ID] = element(
        name="W604",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )
