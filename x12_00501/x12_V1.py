# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class V1(Segment):
    """
    V1 - Vessel Identification
    
    Description:
        To provide vessel details and voyage number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/V1/
    """
    _id: Literal["V1"] = id_element(name="V1")

    VesselCode: Optional[X12ID] = element(
        name="V101",
        description="Vessel Code",
        min_length=1,
        max_length=8,
    )

    VesselName: Optional[X12AN] = element(
        name="V102",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )

    CountryCode: Optional[X12ID] = element(
        name="V103",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    FlightVoyageNumber: Optional[X12AN] = element(
        name="V104",
        description="Flight/Voyage Number",
        min_length=2,
        max_length=10,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="V105",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    VesselRequirementCode: Optional[X12ID] = element(
        name="V106",
        description="Vessel Requirement Code",
        min_length=1,
        max_length=1,
    )

    VesselTypeCode: Optional[X12ID] = element(
        name="V107",
        description="Vessel Type Code",
        min_length=2,
        max_length=2,
    )

    VesselCodeQualifier: Optional[X12ID] = element(
        name="V108",
        description="Vessel Code Qualifier",
        min_length=1,
        max_length=1,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="V109",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )
