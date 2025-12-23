# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RSD(Segment):
    """
    RSD - Residency Information
    
    Description:
        To provide information for establishing residency within a state for tuition purposes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RSD/
    """
    _id: Literal["RSD"] = id_element(name="RSD")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="RSD01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="RSD02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    IndividualRelationshipCode: Optional[X12ID] = element(
        name="RSD03",
        description="Individual Relationship Code",
        min_length=2,
        max_length=2,
    )
