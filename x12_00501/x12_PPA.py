# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PPA(Segment):
    """
    PPA - Property Location
    
    Description:
        To identify a physical property location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PPA/
    """
    _id: Literal["PPA"] = id_element(name="PPA")

    LocationQualifier: X12ID = element(
        name="PPA01",
        description="Location Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: X12AN = element(
        name="PPA02",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    LongitudeCode: Optional[X12ID] = element(
        name="PPA03",
        description="Longitude Code",
        min_length=7,
        max_length=7,
    )

    DirectionIdentifierCode: Optional[X12ID] = element(
        name="PPA04",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )

    LatitudeCode: Optional[X12ID] = element(
        name="PPA05",
        description="Latitude Code",
        min_length=7,
        max_length=7,
    )

    DirectionIdentifierCode2: Optional[X12ID] = element(
        name="PPA06",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )
