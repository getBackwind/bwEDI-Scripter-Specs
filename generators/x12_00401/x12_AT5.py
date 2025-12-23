# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class AT5(Segment):
    """
    AT5 - Bill of Lading Handling Requirements
    
    Description:
        To identify Bill of Lading handling and service requirements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AT5/
    """
    _id: Literal["AT5"] = id_element(name="AT5")

    SpecialHandlingCode: Optional[X12ID] = element(
        name="AT501",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    SpecialServicesCode: Optional[X12ID] = element(
        name="AT502",
        description="Special Services Code",
        min_length=2,
        max_length=3,
    )

    SpecialHandlingDescription: Optional[X12AN] = element(
        name="AT503",
        description="Special Handling Description",
        min_length=2,
        max_length=30,
    )
