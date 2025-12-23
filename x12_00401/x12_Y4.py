# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class Y4(Segment):
    """
    Y4 - Container Release
    
    Description:
        To transmit information relative to containers available for release
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/Y4/
    """
    _id: Literal["Y4"] = id_element(name="Y4")

    BookingNumber: Optional[X12AN] = element(
        name="Y401",
        description="Booking Number",
        min_length=1,
        max_length=17,
    )

    BookingNumber2: Optional[X12AN] = element(
        name="Y402",
        description="Booking Number",
        min_length=1,
        max_length=17,
    )

    Date: Optional[X12DT] = element(
        name="Y403",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="Y404",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    NumberOfContainers: Optional[X12Nn] = element(
        name="Y405",
        description="Number of Containers",
        min_length=1,
        max_length=4,
    )

    EquipmentType: Optional[X12ID] = element(
        name="Y406",
        description="Equipment Type",
        min_length=4,
        max_length=4,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="Y407",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="Y408",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="Y409",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="Y410",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )
