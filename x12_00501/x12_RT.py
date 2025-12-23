# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class RT(Segment):
    """
    RT - Rate Destination
    
    Description:
        To provide destination information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RT/
    """
    _id: Literal["RT"] = id_element(name="RT")

    RateValueQualifier: X12ID = element(
        name="RT01",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="RT02",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    DealerCode: Optional[X12AN] = element(
        name="RT03",
        description="Dealer Code",
        min_length=2,
        max_length=9,
    )

    VehicleServiceCode: Optional[X12ID] = element(
        name="RT04",
        description="Vehicle Service Code",
        min_length=2,
        max_length=2,
    )

    DistanceQualifier: Optional[X12ID] = element(
        name="RT05",
        description="Distance Qualifier",
        min_length=1,
        max_length=1,
    )

    TariffDistance: Optional[X12Nn] = element(
        name="RT06",
        description="Tariff Distance",
        min_length=1,
        max_length=5,
    )

    NationalMotorFreightTransportationAssociationLocationName: Optional[X12AN] = element(
        name="RT07",
        description="National Motor Freight Transportation Association Location Name",
        min_length=2,
        max_length=27,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="RT08",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    Name: Optional[X12AN] = element(
        name="RT09",
        description="Name",
        min_length=1,
        max_length=60,
    )

    AddressInformation: Optional[X12AN] = element(
        name="RT10",
        description="Address Information",
        min_length=1,
        max_length=55,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="RT11",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="RT12",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )
