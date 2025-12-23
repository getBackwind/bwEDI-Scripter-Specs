# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PT(Segment):
    """
    PT - Patron
    
    Description:
        To identify a party involved in a rate docket
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PT/
    """
    _id: Literal["PT"] = id_element(name="PT")

    ConditionSegmentLogicalConnector: X12AN = element(
        name="PT01",
        description="Condition Segment Logical Connector",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="PT02",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    Name30CharacterFormat: Optional[X12AN] = element(
        name="PT03",
        description="Name (30 Character Format)",
        min_length=2,
        max_length=30,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="PT04",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="PT05",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    ChangeTypeCode: Optional[X12ID] = element(
        name="PT06",
        description="Change Type Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="PT07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    DocketControlNumber: Optional[X12AN] = element(
        name="PT08",
        description="Docket Control Number",
        min_length=1,
        max_length=7,
    )

    DocketIdentification: Optional[X12AN] = element(
        name="PT09",
        description="Docket Identification",
        min_length=1,
        max_length=11,
    )

    GroupTitle: Optional[X12AN] = element(
        name="PT10",
        description="Group Title",
        min_length=2,
        max_length=30,
    )

    EntityRelationshipCode: Optional[X12ID] = element(
        name="PT11",
        description="Entity Relationship Code",
        min_length=2,
        max_length=2,
    )
