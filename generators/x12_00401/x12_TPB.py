# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TPB(Segment):
    """
    TPB - Business Professional Title
    
    Description:
        To identify title of an individual within a company
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TPB/
    """
    _id: Literal["TPB"] = id_element(name="TPB")

    BusinessProfessionalTitleCode: Optional[X12ID] = element(
        name="TPB01",
        description="Business Professional Title Code",
        min_length=1,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="TPB02",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="TPB03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="TPB04",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )
