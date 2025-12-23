# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class B9A(Segment):
    """
    B9A - Service Request
    
    Description:
        To identify the specified logistics services requested
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/B9A/
    """
    _id: Literal["B9A"] = id_element(name="B9A")

    ServiceRequestCode: X12ID = element(
        name="B9A01",
        description="Service Request Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )
