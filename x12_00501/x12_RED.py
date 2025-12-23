# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RED(Segment):
    """
    RED - Related Data
    
    Description:
        To provide business data related to an item within a transaction to which a business application editing process has been applied, and an error condition has resulted
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RED/
    """
    _id: Literal["RED"] = id_element(name="RED")

    Description: X12AN = element(
        name="RED01",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )

    RelatedID: Optional[X12ID] = element(
        name="RED02",
        description="Related Data Identification Code",
        min_length=2,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="RED03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="RED04",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="RED05",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="RED06",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
