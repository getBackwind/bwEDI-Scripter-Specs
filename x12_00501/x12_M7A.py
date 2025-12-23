# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class M7A(Segment):
    """
    M7A - Seal Number Replacement
    
    Description:
        To provide an audit trail of seal number changes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M7A/
    """
    _id: Literal["M7A"] = id_element(name="M7A")

    SealNumber: X12AN = element(
        name="M7A01",
        description="Seal Number",
        mandatory=True,
        min_length=2,
        max_length=15,
    )

    SealNumber2: X12AN = element(
        name="M7A02",
        description="Seal Number",
        mandatory=True,
        min_length=2,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="M7A03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="M7A04",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    Name: Optional[X12AN] = element(
        name="M7A05",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Description: Optional[X12AN] = element(
        name="M7A06",
        description="Description",
        min_length=1,
        max_length=80,
    )
