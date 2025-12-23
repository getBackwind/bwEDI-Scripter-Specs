# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class N1(Segment):
    """
    N1 - Name
    
    Description:
        To identify a party by type of organization, name, and code
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N1/
    """
    _id: Literal["N1"] = id_element(name="N1")

    TypeCode: X12ID = element(
        name="N101",
        description="Entity Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    Name: Optional[X12AN] = element(
        name="N102",
        description="Name",
        min_length=1,
        max_length=60,
    )

    IdCodeQualifier: Optional[X12ID] = element(
        name="N103",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdCode: Optional[X12AN] = element(
        name="N104",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    EntityRelationshipCode: Optional[X12ID] = element(
        name="N105",
        description="Entity Relationship Code",
        min_length=2,
        max_length=2,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="N106",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )
