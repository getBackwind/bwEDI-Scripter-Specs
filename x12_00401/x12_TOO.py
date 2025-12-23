# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TOO(Segment):
    """
    TOO - Tooth Identification
    
    Description:
        To identify a tooth by number and, if applicable, one or more tooth surfaces
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TOO/
    """
    _id: Literal["TOO"] = id_element(name="TOO")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="TOO01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="TOO02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
