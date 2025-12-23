# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class L10(Segment):
    """
    L10 - Weight Information
    
    Description:
        To transmit weight information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/L10/
    """
    _id: Literal["L10"] = id_element(name="L10")

    Weight: X12R = element(
        name="L1001",
        description="Weight",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    WeightQualifier: X12ID = element(
        name="L1002",
        description="Weight Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="L1003",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )
