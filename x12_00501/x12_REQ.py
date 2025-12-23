# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class REQ(Segment):
    """
    REQ - Request Information
    
    Description:
        To identify the requested limitations and the corresponding response actions of an inquiry
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/REQ/
    """
    _id: Literal["REQ"] = id_element(name="REQ")

    InquiryResponseCode: Optional[X12ID] = element(
        name="REQ01",
        description="Inquiry Response Code",
        min_length=1,
        max_length=2,
    )

    InquirySelectionCode: Optional[X12ID] = element(
        name="REQ02",
        description="Inquiry Selection Code",
        min_length=1,
        max_length=2,
    )
