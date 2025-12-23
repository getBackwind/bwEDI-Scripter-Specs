# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class REF(Segment):
    """
    REF - Reference Identification
    
    Description:
        To specify identifying information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/REF/
    """
    _id: Literal["REF"] = id_element(name="REF")

    Qualifier: X12ID = element(
        name="REF01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ID: Optional[X12AN] = element(
        name="REF02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="REF03",
        description="Description",
        min_length=1,
        max_length=80,
    )
