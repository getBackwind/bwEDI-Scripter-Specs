# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class Y6(Segment):
    """
    Y6 - Authentication
    
    Description:
        To specify the authority for authorizing an action and the date authentication is made
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/Y6/
    """
    _id: Literal["Y6"] = id_element(name="Y6")

    AuthorityIdentifierCode: Optional[X12ID] = element(
        name="Y601",
        description="Authority Identifier Code",
        min_length=2,
        max_length=2,
    )

    Authority: X12AN = element(
        name="Y602",
        description="Authority",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    AuthorizationDate: X12DT = element(
        name="Y603",
        description="Authorization Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )
