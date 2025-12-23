# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class NX1(Segment):
    """
    NX1 - Property or Entity Identification
    
    Description:
        To define the attributes of a property or an entity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/NX1/
    """
    _id: Literal["NX1"] = id_element(name="NX1")

    EntityIdentifierCode: X12ID = element(
        name="NX101",
        description="Entity Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    EntityIdentifierCode2: Optional[X12ID] = element(
        name="NX102",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    EntityIdentifierCode3: Optional[X12ID] = element(
        name="NX103",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    EntityIdentifierCode4: Optional[X12ID] = element(
        name="NX104",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    EntityIdentifierCode5: Optional[X12ID] = element(
        name="NX105",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )
