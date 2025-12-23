# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class NX2(Segment):
    """
    NX2 - Location ID Component
    
    Description:
        To define types and values of a geographic location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/NX2/
    """
    _id: Literal["NX2"] = id_element(name="NX2")

    AddressComponentQualifier: X12ID = element(
        name="NX201",
        description="Address Component Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AddressInformation: X12AN = element(
        name="NX202",
        description="Address Information",
        mandatory=True,
        min_length=1,
        max_length=55,
    )

    CountyDesignator: Optional[X12ID] = element(
        name="NX203",
        description="County Designator",
        min_length=5,
        max_length=5,
    )
