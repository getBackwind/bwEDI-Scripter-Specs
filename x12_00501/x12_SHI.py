# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SHI(Segment):
    """
    SHI - Security Holding Information
    
    Description:
        To specify information concerning securities held by an entity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SHI/
    """
    _id: Literal["SHI"] = id_element(name="SHI")

    SecurityHoldingTypeCode: X12ID = element(
        name="SHI01",
        description="Security Holding Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Name: Optional[X12AN] = element(
        name="SHI02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SHI03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ProductTransferTypeCode: Optional[X12ID] = element(
        name="SHI04",
        description="Product Transfer Type Code",
        min_length=2,
        max_length=2,
    )

    StatusCode: Optional[X12ID] = element(
        name="SHI05",
        description="Status Code",
        min_length=2,
        max_length=2,
    )
