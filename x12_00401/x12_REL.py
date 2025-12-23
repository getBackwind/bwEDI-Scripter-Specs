# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class REL(Segment):
    """
    REL - Relationship
    
    Description:
        To specify relationship and birth order of entity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/REL/
    """
    _id: Literal["REL"] = id_element(name="REL")

    IndividualRelationshipCode: X12ID = element(
        name="REL01",
        description="Individual Relationship Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Number: Optional[X12Nn] = element(
        name="REL02",
        description="Number",
        min_length=1,
        max_length=9,
    )
