# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TD5(Segment):
    """
    TD5 - Carrier Details (Routing Sequence/Transit Time)
    
    Description:
        To specify the carrier and sequence of routing and provide transit time information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TD5/
    """
    _id: Literal["TD5"] = id_element(name="TD5")

    RelationshipQualifier: Optional[X12ID] = element(
        name="TD501",
        description="Routing Sequence Code",
        min_length=1,
        max_length=2,
    )

    IdQualifier: Optional[X12ID] = element(
        name="TD502",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdCode: Optional[X12AN] = element(
        name="TD503",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    TransportationCode: Optional[X12ID] = element(
        name="TD504",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    Routing: Optional[X12AN] = element(
        name="TD505",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    ShipmentOrderStatusCode: Optional[X12ID] = element(
        name="TD506",
        description="Shipment/Order Status Code",
        min_length=2,
        max_length=2,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="TD507",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationID: Optional[X12AN] = element(
        name="TD508",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    TransitDirectionCode: Optional[X12ID] = element(
        name="TD509",
        description="Transit Direction Code",
        min_length=2,
        max_length=2,
    )

    TransitTimeDirectionQualifier: Optional[X12ID] = element(
        name="TD510",
        description="Transit Time Direction Qualifier",
        min_length=2,
        max_length=2,
    )

    TransitTime: Optional[X12R] = element(
        name="TD511",
        description="Transit Time",
        min_length=1,
        max_length=4,
    )

    ServiceLevelCode: Optional[X12ID] = element(
        name="TD512",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    ServiceLevelCode2: Optional[X12ID] = element(
        name="TD513",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    ServiceLevelCode3: Optional[X12ID] = element(
        name="TD514",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="TD515",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
