# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class ENT(Segment):
    """
    ENT - Entity
    
    Description:
        To designate the entities which are parties to a transaction and specify a reference meaningful to those entities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ENT/
    """
    _id: Literal["ENT"] = id_element(name="ENT")

    AssignedNumber: Optional[X12Nn] = element(
        name="ENT01",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="ENT02",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="ENT03",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="ENT04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    EntityIdentifierCode2: Optional[X12ID] = element(
        name="ENT05",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="ENT06",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="ENT07",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="ENT08",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ENT09",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
