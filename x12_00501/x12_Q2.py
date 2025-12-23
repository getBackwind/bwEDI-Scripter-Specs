# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R


class Q2(Segment):
    """
    Q2 - Status Details (Ocean)
    
    Description:
        To transmit identifying information relative to identification of vessel, transportation dates, lading quantity, weight, and cube
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/Q2/
    """
    _id: Literal["Q2"] = id_element(name="Q2")

    VesselCode: Optional[X12ID] = element(
        name="Q201",
        description="Vessel Code",
        min_length=1,
        max_length=8,
    )

    CountryCode: Optional[X12ID] = element(
        name="Q202",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="Q203",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="Q204",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: Optional[X12DT] = element(
        name="Q205",
        description="Date",
        min_length=8,
        max_length=8,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="Q206",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )

    Weight: Optional[X12R] = element(
        name="Q207",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="Q208",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    FlightVoyageNumber: Optional[X12AN] = element(
        name="Q209",
        description="Flight/Voyage Number",
        min_length=2,
        max_length=10,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="Q210",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="Q211",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    VesselCodeQualifier: Optional[X12ID] = element(
        name="Q212",
        description="Vessel Code Qualifier",
        min_length=1,
        max_length=1,
    )

    VesselName: Optional[X12AN] = element(
        name="Q213",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )

    Volume: Optional[X12R] = element(
        name="Q214",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="Q215",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="Q216",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )
