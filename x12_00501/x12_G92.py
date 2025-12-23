# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class G92(Segment):
    """
    G92 - Purchase Order Change Type
    
    Description:
        To identify the reason for a change to a previously transmitted purchase order
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G92/
    """
    _id: Literal["G92"] = id_element(name="G92")

    ChangeOrResponseTypeCode: X12ID = element(
        name="G9201",
        description="Change or Response Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="G9202",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    PurchaseOrderNumber: X12AN = element(
        name="G9203",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )
