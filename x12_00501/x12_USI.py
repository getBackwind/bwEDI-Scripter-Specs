# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class USI(Segment):
    """
    USI - Unitized Shipment Information
    
    Description:
        To specify the quantity, number of pallet spaces and stackability of unitized units
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/USI/
    """
    _id: Literal["USI"] = id_element(name="USI")

    Quantity: X12R = element(
        name="USI01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    PackagingFormCode: X12ID = element(
        name="USI02",
        description="Packaging Form Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="USI03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
