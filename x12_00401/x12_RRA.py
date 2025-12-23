# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RRA(Segment):
    """
    RRA - Required Response
    
    Description:
        To indicate information that is required to be included in the response
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RRA/
    """
    _id: Literal["RRA"] = id_element(name="RRA")

    InformationType: X12ID = element(
        name="RRA01",
        description="Information Type",
        mandatory=True,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="RRA02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
