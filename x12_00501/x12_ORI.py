# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class ORI(Segment):
    """
    ORI - Object Reference Identification
    
    Description:
        To identify the object identification reference
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ORI/
    """
    _id: Literal["ORI"] = id_element(name="ORI")

    AssociatedObjectReferenceIdentification: X12AN = element(
        name="ORI01",
        description="Associated Object Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=36,
    )
