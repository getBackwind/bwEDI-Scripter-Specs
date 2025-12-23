# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class AK2(Segment):
    """
    AK2 - Transaction Set Response Header
    
    Description:
        To start acknowledgment of a single transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AK2/
    """
    _id: Literal["AK2"] = id_element(name="AK2")

    TransactionSetCode: X12ID = element(
        name="AK201",
        description="Transaction Set Identifier Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    TransactionSetID: X12AN = element(
        name="AK202",
        description="Transaction Set Control Number",
        mandatory=True,
        min_length=4,
        max_length=9,
    )
