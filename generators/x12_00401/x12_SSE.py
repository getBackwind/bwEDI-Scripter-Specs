# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12Nn


class SSE(Segment):
    """
    SSE - Entry and Exit Information
    
    Description:
        To provide information concerning the entry into or withdrawal from a school, school program, school district, or postsecondary institution
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SSE/
    """
    _id: Literal["SSE"] = id_element(name="SSE")

    Date: Optional[X12DT] = element(
        name="SSE01",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="SSE02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="SSE03",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    Number: Optional[X12Nn] = element(
        name="SSE04",
        description="Number",
        min_length=1,
        max_length=9,
    )
