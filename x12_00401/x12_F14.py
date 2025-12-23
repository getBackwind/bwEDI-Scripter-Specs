# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class F14(Segment):
    """
    F14 - Line Item Reject
    
    Description:
        To identify the specific reasons why individual line items of a claim or part of a claim are rejected
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/F14/
    """
    _id: Literal["F14"] = id_element(name="F14")

    AssignedNumber: X12Nn = element(
        name="F1401",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    DeclineAmendReasonCode: X12ID = element(
        name="F1402",
        description="Decline/Amend Reason Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )
