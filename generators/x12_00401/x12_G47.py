# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT


class G47(Segment):
    """
    G47 - Statement Identification
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G47/
    """
    _id: Literal["G47"] = id_element(name="G47")

    Date: X12DT = element(
        name="G4701",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    StatementNumber: X12AN = element(
        name="G4702",
        description="Statement Number",
        mandatory=True,
        min_length=1,
        max_length=16,
    )
