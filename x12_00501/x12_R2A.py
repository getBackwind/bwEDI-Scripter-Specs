# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class R2A(Segment):
    """
    R2A - Route Information with Preference
    
    Description:
        To specify the responsibilities and carrier preference
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R2A/
    """
    _id: Literal["R2A"] = id_element(name="R2A")

    RoutingSequenceCode: X12ID = element(
        name="R2A01",
        description="Routing Sequence Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Preference: X12ID = element(
        name="R2A02",
        description="Preference",
        mandatory=True,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="R2A03",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="R2A04",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="R2A05",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="R2A06",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="R2A07",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )

    RouteCode: Optional[X12AN] = element(
        name="R2A08",
        description="Route Code",
        min_length=1,
        max_length=13,
    )

    RouteDescription: Optional[X12AN] = element(
        name="R2A09",
        description="Route Description",
        min_length=1,
        max_length=35,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="R2A10",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )
