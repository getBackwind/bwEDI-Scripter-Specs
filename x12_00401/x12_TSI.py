# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TSI(Segment):
    """
    TSI - Automatic Equipment Tag Status Information
    
    Description:
        To indicate the status of an automatic equipment identification tag and associated information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TSI/
    """
    _id: Literal["TSI"] = id_element(name="TSI")

    TagStatusCode: Optional[X12ID] = element(
        name="TSI01",
        description="Tag Status Code",
        min_length=1,
        max_length=1,
    )

    IndustryCode: Optional[X12AN] = element(
        name="TSI02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Quantity: Optional[X12R] = element(
        name="TSI03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="TSI04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
