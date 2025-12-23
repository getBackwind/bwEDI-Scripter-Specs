# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PKD(Segment):
    """
    PKD - Packaging Description
    
    Description:
        To specify a package description and other information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PKD/
    """
    _id: Literal["PKD"] = id_element(name="PKD")

    PackagingCode: Optional[X12AN] = element(
        name="PKD01",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="PKD02",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="PKD03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    PackagingDescriptionCode: Optional[X12AN] = element(
        name="PKD04",
        description="Packaging Description Code",
        min_length=1,
        max_length=7,
    )

    OwnershipCode: Optional[X12ID] = element(
        name="PKD05",
        description="Ownership Code",
        min_length=1,
        max_length=1,
    )
