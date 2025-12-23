# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class M15(Segment):
    """
    M15 - Customs Events Advisory Details
    
    Description:
        To notify Customs of in-bond cargo movement or of a conveyance arrival or departure, or of transfer of custodial liability when an in-bond movement involves multiple legs
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M15/
    """
    _id: Literal["M15"] = id_element(name="M15")

    NotificationEntityQualifier: X12AN = element(
        name="M1501",
        description="Notification Entity Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="M1502",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: X12DT = element(
        name="M1503",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="M1504",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="M1505",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Time: X12TM = element(
        name="M1506",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    SealNumber: Optional[X12AN] = element(
        name="M1507",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="M1508",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="M1509",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    CityName: Optional[X12AN] = element(
        name="M1510",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="M1511",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="M1512",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="M1513",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="M1514",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    VesselName: Optional[X12AN] = element(
        name="M1515",
        description="Vessel Name",
        min_length=2,
        max_length=28,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="M1516",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="M1517",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )
