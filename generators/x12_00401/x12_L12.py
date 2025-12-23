# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class L12(Segment):
    """
    L12 - Alternate Lading Description
    
    Description:
        To provide lading description beyond what is required for rating and billing purposes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/L12/
    """
    _id: Literal["L12"] = id_element(name="L12")

    LadingDescriptionQualifier: Optional[X12ID] = element(
        name="L1201",
        description="Lading Description Qualifier",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="L1202",
        description="Description",
        min_length=1,
        max_length=80,
    )
