# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class UCS(Segment):
    """
    UCS - Underwriting Considerations
    
    Description:
        To report personal health and medical history data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/UCS/
    """
    _id: Literal["UCS"] = id_element(name="UCS")

    CodeCategory: Optional[X12ID] = element(
        name="UCS01",
        description="Code Category",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="UCS02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ItemDescriptionType: Optional[X12ID] = element(
        name="UCS03",
        description="Item Description Type",
    )

    Description2: Optional[X12AN] = element(
        name="UCS04",
        description="Description",
        min_length=1,
        max_length=80,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="UCS05",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="UCS06",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Number: Optional[X12Nn] = element(
        name="UCS07",
        description="Number",
        min_length=1,
        max_length=9,
    )
