# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class INR(Segment):
    """
    INR - Information Request
    
    Description:
        To specify the type and status of information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/INR/
    """
    _id: Literal["INR"] = id_element(name="INR")

    CodeCategory: X12ID = element(
        name="INR01",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    InformationType: X12ID = element(
        name="INR02",
        description="Information Type",
        mandatory=True,
    )

    InformationStatusCode: Optional[X12ID] = element(
        name="INR03",
        description="Information Status Code",
        min_length=1,
        max_length=1,
    )
