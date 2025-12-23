# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class SHR(Segment):
    """
    SHR - Railroad Interline Service Special Handling Restrictions
    
    Description:
        To identify the special handling codes that apply to a shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SHR/
    """
    _id: Literal["SHR"] = id_element(name="SHR")

    YesNoConditionOrResponseCode: X12ID = element(
        name="SHR01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    SpecialHandlingCode: Optional[X12ID] = element(
        name="SHR02",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )
