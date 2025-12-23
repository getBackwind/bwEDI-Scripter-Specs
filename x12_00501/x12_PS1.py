# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PS1(Segment):
    """
    PS1 - Purchase Service
    
    Description:
        To specify the information about services that are purchased
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PS1/
    """
    _id: Literal["PS1"] = id_element(name="PS1")

    ReferenceIdentification: X12AN = element(
        name="PS101",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    MonetaryAmount: X12R = element(
        name="PS102",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="PS103",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
