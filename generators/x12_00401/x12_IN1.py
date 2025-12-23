# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class IN1(Segment):
    """
    IN1 - Individual Identification
    
    Description:
        To provide identification of an individual or entity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IN1/
    """
    _id: Literal["IN1"] = id_element(name="IN1")

    EntityTypeQualifier: X12ID = element(
        name="IN101",
        description="Entity Type Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    NameTypeCode: X12ID = element(
        name="IN102",
        description="Name Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="IN103",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="IN104",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="IN105",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    IndividualRelationshipCode: Optional[X12ID] = element(
        name="IN106",
        description="Individual Relationship Code",
        min_length=2,
        max_length=2,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="IN107",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )
