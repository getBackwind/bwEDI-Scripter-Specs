# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class ERP(Segment):
    """
    ERP - Educational Record Purpose
    
    Description:
        To indicate the type of educational record or information being requested or being sent and to specify conditions under which it is being requested or was sent
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ERP/
    """
    _id: Literal["ERP"] = id_element(name="ERP")

    TransactionTypeCode: X12ID = element(
        name="ERP01",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="ERP02",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    ActionCode: Optional[X12ID] = element(
        name="ERP03",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
