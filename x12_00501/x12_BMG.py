# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BMG(Segment):
    """
    BMG - Beginning Segment For Text Message
    
    Description:
        To indicate the beginning of a Text Message Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BMG/
    """
    _id: Literal["BMG"] = id_element(name="BMG")

    TransactionSetPurposeCode: X12ID = element(
        name="BMG01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="BMG02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BMG03",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
