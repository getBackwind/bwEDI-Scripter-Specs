# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class B2A(Segment):
    """
    B2A - Set Purpose
    
    Description:
        To allow for positive identification of transaction set purpose
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/B2A/
    """
    _id: Literal["B2A"] = id_element(name="B2A")

    TransactionSetPurposeCode: X12ID = element(
        name="B2A01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ApplicationType: Optional[X12ID] = element(
        name="B2A02",
        description="Application Type",
    )
