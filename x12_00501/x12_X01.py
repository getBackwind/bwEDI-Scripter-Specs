# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class X01(Segment):
    """
    X01 - Automated Manifest Archive Status Details
    
    Description:
        To specify the automated manifest in the U.S. Customs system that is pending archive or actually archived
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/X01/
    """
    _id: Literal["X01"] = id_element(name="X01")

    StandardCarrierAlphaCode: X12ID = element(
        name="X0101",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    LocationQualifier: X12ID = element(
        name="X0102",
        description="Location Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: X12AN = element(
        name="X0103",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    VesselCodeQualifier: Optional[X12ID] = element(
        name="X0104",
        description="Vessel Code Qualifier",
        min_length=1,
        max_length=1,
    )

    VesselCode: Optional[X12ID] = element(
        name="X0105",
        description="Vessel Code",
        min_length=1,
        max_length=8,
    )

    VesselName: Optional[X12AN] = element(
        name="X0106",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )

    FlightVoyageNumber: Optional[X12AN] = element(
        name="X0107",
        description="Flight/Voyage Number",
        min_length=2,
        max_length=10,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="X0108",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="X0109",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Quantity: Optional[X12R] = element(
        name="X0110",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
