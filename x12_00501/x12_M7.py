# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class M7(Segment):
    """
    M7 - Seal Numbers
    
    Description:
        To record seal numbers used and the organization that applied the seals
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M7/
    """
    _id: Literal["M7"] = id_element(name="M7")

    SealNumber: X12AN = element(
        name="M701",
        description="Seal Number",
        mandatory=True,
        min_length=2,
        max_length=15,
    )

    SealNumber2: Optional[X12AN] = element(
        name="M702",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealNumber3: Optional[X12AN] = element(
        name="M703",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealNumber4: Optional[X12AN] = element(
        name="M704",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="M705",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )
