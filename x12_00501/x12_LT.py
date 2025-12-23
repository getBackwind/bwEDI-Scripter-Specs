# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LT(Segment):
    """
    LT - Letter of Recommendation
    
    Description:
        To provide information about a letter of recommendation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LT/
    """
    _id: Literal["LT"] = id_element(name="LT")

    IndividualRelationshipCode: X12ID = element(
        name="LT01",
        description="Individual Relationship Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="LT02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Name: Optional[X12AN] = element(
        name="LT03",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Description2: Optional[X12AN] = element(
        name="LT04",
        description="Description",
        min_length=1,
        max_length=80,
    )
