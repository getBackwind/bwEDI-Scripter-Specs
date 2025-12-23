# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PDS(Segment):
    """
    PDS - Property Description/Legal Description
    
    Description:
        To provide specifics on property or legal description; this segment provides for a simple legal description such as lot, block and subdivision
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PDS/
    """
    _id: Literal["PDS"] = id_element(name="PDS")

    PropertyDescriptionQualifier: X12ID = element(
        name="PDS01",
        description="Property Description Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="PDS02",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )
