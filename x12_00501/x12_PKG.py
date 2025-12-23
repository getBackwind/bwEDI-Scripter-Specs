# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PKG(Segment):
    """
    PKG - Marking, Packaging, Loading
    
    Description:
        To describe marking, packaging, loading, and unloading requirements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PKG/
    """
    _id: Literal["PKG"] = id_element(name="PKG")

    PKG01: Optional[X12ID] = element(
        name="PKG01",
        description="Item Description Type",
    )

    PKG02: Optional[X12ID] = element(
        name="PKG02",
        description="Packaging Characteristic Code",
        min_length=2,
        max_length=3,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="PKG03",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    PackagingDescriptionCode: Optional[X12AN] = element(
        name="PKG04",
        description="Packaging Description Code",
        min_length=1,
        max_length=7,
    )

    Description: Optional[X12AN] = element(
        name="PKG05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    UnitLoadOptionCode: Optional[X12ID] = element(
        name="PKG06",
        description="Unit Load Option Code",
        min_length=2,
        max_length=2,
    )
