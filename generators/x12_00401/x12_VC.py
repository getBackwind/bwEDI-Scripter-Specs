# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class VC(Segment):
    """
    VC - Motor Vehicle Control
    
    Description:
        To define motor vehicle identification and logistics
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/VC/
    """
    _id: Literal["VC"] = id_element(name="VC")

    VehicleIdentificationNumber: X12AN = element(
        name="VC01",
        description="Vehicle Identification Number",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    VehicleDeckPositionCode: Optional[X12ID] = element(
        name="VC02",
        description="Vehicle Deck Position Code",
        min_length=2,
        max_length=2,
    )

    VehicleTypeCode: Optional[X12ID] = element(
        name="VC03",
        description="Vehicle Type Code",
        min_length=1,
        max_length=1,
    )

    DealerCode: Optional[X12AN] = element(
        name="VC04",
        description="Dealer Code",
        min_length=2,
        max_length=9,
    )

    RouteCode: Optional[X12AN] = element(
        name="VC05",
        description="Route Code",
        min_length=1,
        max_length=13,
    )

    BayLocation: Optional[X12AN] = element(
        name="VC06",
        description="Bay Location",
        min_length=1,
        max_length=6,
    )

    AutomotiveManufacturersCode: Optional[X12ID] = element(
        name="VC07",
        description="Automotive Manufacturers Code",
        min_length=2,
        max_length=2,
    )

    DamageExceptionIndicator: Optional[X12ID] = element(
        name="VC08",
        description="Damage Exception Indicator",
    )

    SupplementalInspectionCode: Optional[X12ID] = element(
        name="VC09",
        description="Supplemental Inspection Code",
        min_length=1,
        max_length=1,
    )

    FactoryCarOrderNumber: Optional[X12AN] = element(
        name="VC10",
        description="Factory Car Order Number",
        min_length=6,
        max_length=10,
    )

    VesselStowageLocation: Optional[X12AN] = element(
        name="VC11",
        description="Vessel Stowage Location",
        min_length=1,
        max_length=12,
    )
