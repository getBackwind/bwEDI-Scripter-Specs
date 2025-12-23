# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class M12(Segment):
    """
    M12 - In-bond Identifying Information
    
    Description:
        To transmit in-bond information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/M12/
    """
    _id: Literal["M12"] = id_element(name="M12")

    CustomsEntryTypeCode: X12ID = element(
        name="M1201",
        description="Customs Entry Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CustomsEntryNumber: Optional[X12AN] = element(
        name="M1202",
        description="Customs Entry Number",
        min_length=1,
        max_length=15,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="M1203",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="M1204",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    CustomsShipmentValue: Optional[X12AN] = element(
        name="M1205",
        description="Customs Shipment Value",
        min_length=2,
        max_length=8,
    )

    InBondControlNumber: Optional[X12AN] = element(
        name="M1206",
        description="In-bond Control Number",
        min_length=1,
        max_length=25,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="M1207",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="M1208",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="M1209",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="M1210",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    VesselName: Optional[X12AN] = element(
        name="M1211",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )
