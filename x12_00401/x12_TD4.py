# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TD4(Segment):
    """
    TD4 - Carrier Details (Special Handling, or Hazardous Materials, or Both)
    
    Description:
        To specify transportation special handling requirements, or hazardous materials information, or both
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TD4/
    """
    _id: Literal["TD4"] = id_element(name="TD4")

    SpecialHandlingCode: Optional[X12ID] = element(
        name="TD401",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    HazardousMaterialCodeQualifier: Optional[X12ID] = element(
        name="TD402",
        description="Hazardous Material Code Qualifier",
        min_length=1,
        max_length=1,
    )

    HazardousMaterialClassCode: Optional[X12AN] = element(
        name="TD403",
        description="Hazardous Material Class Code",
        min_length=1,
        max_length=4,
    )

    Description: Optional[X12AN] = element(
        name="TD404",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="TD405",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
