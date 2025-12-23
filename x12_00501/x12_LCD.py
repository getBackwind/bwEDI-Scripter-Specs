# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class LCD(Segment):
    """
    LCD - Place/Location Description
    
    Description:
        To further define and describe a place or location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LCD/
    """
    _id: Literal["LCD"] = id_element(name="LCD")

    AssignedIdentification: Optional[X12AN] = element(
        name="LCD01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="LCD02",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    ActionCode: Optional[X12ID] = element(
        name="LCD03",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="LCD04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="LCD05",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="LCD06",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
