# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LIE(Segment):
    """
    LIE - Individual or Event Location
    
    Description:
        To provide an accurate description of where an individual was located or an event took place
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LIE/
    """
    _id: Literal["LIE"] = id_element(name="LIE")

    LocationTypeCode: X12ID = element(
        name="LIE01",
        description="Location Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProximityCode: Optional[X12ID] = element(
        name="LIE02",
        description="Proximity Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="LIE03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="LIE04",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )
