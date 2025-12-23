# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MS1(Segment):
    """
    MS1 - Equipment, Shipment, or Real Property Location
    
    Description:
        To specify the location of a piece of equipment, a shipment, or real property in terms of city and state or longitude and latitude or postal code
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MS1/
    """
    _id: Literal["MS1"] = id_element(name="MS1")

    CityName: Optional[X12AN] = element(
        name="MS101",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="MS102",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="MS103",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    LongitudeCode: Optional[X12ID] = element(
        name="MS104",
        description="Longitude Code",
        min_length=7,
        max_length=7,
    )

    LatitudeCode: Optional[X12ID] = element(
        name="MS105",
        description="Latitude Code",
        min_length=7,
        max_length=7,
    )

    DirectionIdentifierCode: Optional[X12ID] = element(
        name="MS106",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )

    DirectionIdentifierCode2: Optional[X12ID] = element(
        name="MS107",
        description="Direction Identifier Code",
        min_length=1,
        max_length=1,
    )

    PostalCode: Optional[X12ID] = element(
        name="MS108",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )
