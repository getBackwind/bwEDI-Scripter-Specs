# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class G53(Segment):
    """
    G53 - Maintenance Type
    
    Description:
        To identify the specific type of item maintenance
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G53/
    """
    _id: Literal["G53"] = id_element(name="G53")

    MaintenanceTypeCode: X12ID = element(
        name="G5301",
        description="Maintenance Type Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )
