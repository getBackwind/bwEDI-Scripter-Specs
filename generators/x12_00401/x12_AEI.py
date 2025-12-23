# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class AEI(Segment):
    """
    AEI - Equipment Information Summary
    
    Description:
        To provide summary information on equipment type and count
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AEI/
    """
    _id: Literal["AEI"] = id_element(name="AEI")

    EquipmentDescriptionCode: X12ID = element(
        name="AEI01",
        description="Equipment Description Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="AEI02",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="AEI03",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
