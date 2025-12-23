# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class NM1(Segment):
    """
    NM1 - Individual or Organizational Name
    
    Description:
        To supply the full name of an individual or organizational entity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/NM1/
    """
    _id: Literal["NM1"] = id_element(name="NM1")

    EntityIdentifierCode: X12ID = element(
        name="NM101",
        description="Entity Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    EntityTypeQualifier: X12ID = element(
        name="NM102",
        description="Entity Type Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    NameLastOrOrganizationName: Optional[X12AN] = element(
        name="NM103",
        description="Name Last or Organization Name",
        min_length=1,
        max_length=35,
    )

    NameFirst: Optional[X12AN] = element(
        name="NM104",
        description="Name First",
        min_length=1,
        max_length=25,
    )

    NameMiddle: Optional[X12AN] = element(
        name="NM105",
        description="Name Middle",
        min_length=1,
        max_length=25,
    )

    NamePrefix: Optional[X12AN] = element(
        name="NM106",
        description="Name Prefix",
        min_length=1,
        max_length=10,
    )

    NameSuffix: Optional[X12AN] = element(
        name="NM107",
        description="Name Suffix",
        min_length=1,
        max_length=10,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="NM108",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="NM109",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    EntityRelationshipCode: Optional[X12ID] = element(
        name="NM110",
        description="Entity Relationship Code",
        min_length=2,
        max_length=2,
    )

    EntityIdentifierCode2: Optional[X12ID] = element(
        name="NM111",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )
