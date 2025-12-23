# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class UR(Segment):
    """
    UR - Peer Review Organization or Utilization Review
    
    Description:
        To specify the results of the utilization review
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/UR/
    """
    _id: Literal["UR"] = id_element(name="UR")

    ApprovalCode: X12ID = element(
        name="UR01",
        description="Approval Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="UR02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
