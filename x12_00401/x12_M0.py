# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT


class M0(Segment):
    """
    M0 - Letter of Credit Reference
    
    Description:
        To transmit letter of credit details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/M0/
    """
    _id: Literal["M0"] = id_element(name="M0")

    LetterOfCreditNumber: X12AN = element(
        name="M001",
        description="Letter of Credit Number",
        mandatory=True,
        min_length=2,
        max_length=40,
    )

    Date: Optional[X12DT] = element(
        name="M002",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="M003",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: Optional[X12DT] = element(
        name="M004",
        description="Date",
        min_length=8,
        max_length=8,
    )
