# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class Y1(Segment):
    """
    Y1 - Space Reservation Request
    
    Description:
        To specify information used to make a reservation for space on an ocean vessel
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/Y1/
    """
    _id: Literal["Y1"] = id_element(name="Y1")

    SailingFlightDateEstimated: Optional[X12DT] = element(
        name="Y101",
        description="Sailing/Flight Date Estimated",
        min_length=8,
        max_length=8,
    )

    Date: Optional[X12DT] = element(
        name="Y102",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="Y103",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="Y104",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="Y105",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    CityName: Optional[X12AN] = element(
        name="Y106",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="Y107",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    TariffServiceCode: Optional[X12ID] = element(
        name="Y108",
        description="Tariff Service Code",
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="Y109",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )
