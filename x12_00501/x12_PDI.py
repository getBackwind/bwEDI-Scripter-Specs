# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class PDI(Segment):
    """
    PDI - Practice Detail Information
    
    Description:
        To provide detail information on a health care provider's practice
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PDI/
    """
    _id: Literal["PDI"] = id_element(name="PDI")

    GenderCode: Optional[X12ID] = element(
        name="PDI01",
        description="Gender Code",
        min_length=1,
        max_length=1,
    )

    RangeMinimum: Optional[X12R] = element(
        name="PDI02",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="PDI03",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PDI04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
