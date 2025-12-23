# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class M10(Segment):
    """
    M10 - Manifest Identifying Information
    
    Description:
        To transmit manifest identifying information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/M10/
    """
    _id: Literal["M10"] = id_element(name="M10")

    StandardCarrierAlphaCode: X12ID = element(
        name="M1001",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    TransportationMethodTypeCode: X12ID = element(
        name="M1002",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CountryCode: X12ID = element(
        name="M1003",
        description="Country Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    VesselCode: Optional[X12ID] = element(
        name="M1004",
        description="Vessel Code",
        min_length=1,
        max_length=8,
    )

    VesselName: Optional[X12AN] = element(
        name="M1005",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )

    FlightVoyageNumber: X12AN = element(
        name="M1006",
        description="Flight/Voyage Number",
        mandatory=True,
        min_length=2,
        max_length=10,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="M1007",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Quantity: Optional[X12R] = element(
        name="M1008",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ManifestTypeCode: X12ID = element(
        name="M1009",
        description="Manifest Type Code",
        mandatory=True,
    )

    VesselCodeQualifier: Optional[X12ID] = element(
        name="M1010",
        description="Vessel Code Qualifier",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="M1011",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="M1012",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
