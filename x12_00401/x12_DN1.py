# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DN1(Segment):
    """
    DN1 - Orthodontic Information
    
    Description:
        To supply orthodontic information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DN1/
    """
    _id: Literal["DN1"] = id_element(name="DN1")

    Quantity: Optional[X12R] = element(
        name="DN101",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="DN102",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DN103",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="DN104",
        description="Description",
        min_length=1,
        max_length=80,
    )
