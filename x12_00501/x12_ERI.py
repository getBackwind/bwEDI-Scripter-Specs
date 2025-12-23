# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class ERI(Segment):
    """
    ERI - Entity Relationship
    
    Description:
        To identify the explicit relationship between entities, i.e., parent, child, peer
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ERI/
    """
    _id: Literal["ERI"] = id_element(name="ERI")

    IdentificationCodeQualifier: X12ID = element(
        name="ERI01",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="ERI02",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    EntityRelationshipCode: X12ID = element(
        name="ERI03",
        description="Entity Relationship Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="ERI04",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="ERI05",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    EntityRelationshipCode2: X12ID = element(
        name="ERI06",
        description="Entity Relationship Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    EntityRelationshipCode3: Optional[X12ID] = element(
        name="ERI07",
        description="Entity Relationship Code",
        min_length=2,
        max_length=2,
    )

    EntityRelationshipCode4: Optional[X12ID] = element(
        name="ERI08",
        description="Entity Relationship Code",
        min_length=2,
        max_length=2,
    )

    HierarchyCode: Optional[X12AN] = element(
        name="ERI09",
        description="Hierarchy Code",
        min_length=2,
        max_length=2,
    )
