# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SVA(Segment):
    """
    SVA - Security Value
    
    Description:
        To provide the encoded output of a cryptographic algorithm
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SVA/
    """
    _id: Literal["SVA"] = id_element(name="SVA")

    FilterIDCode: X12ID = element(
        name="SVA01",
        description="Filter ID Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    VersionIdentifier: X12AN = element(
        name="SVA02",
        description="Version Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )
