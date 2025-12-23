# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class VEH(Segment):
    """
    VEH - Vehicle Information
    
    Description:
        To provide descriptions that identify a specific vehicle
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/VEH/
    """
    _id: Literal["VEH"] = id_element(name="VEH")

    AssignedNumber: Optional[X12Nn] = element(
        name="VEH01",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    VehicleIdentificationNumber: Optional[X12AN] = element(
        name="VEH02",
        description="Vehicle Identification Number",
        min_length=1,
        max_length=30,
    )

    Year: Optional[X12Nn] = element(
        name="VEH03",
        description="Year",
        min_length=4,
        max_length=4,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="VEH04",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="VEH05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="VEH06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification3: Optional[X12AN] = element(
        name="VEH07",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Length: Optional[X12R] = element(
        name="VEH08",
        description="Length",
        min_length=1,
        max_length=8,
    )

    ReferenceIdentification4: Optional[X12AN] = element(
        name="VEH09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="VEH10",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="VEH11",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="VEH12",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Amount: Optional[X12Nn] = element(
        name="VEH13",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="VEH14",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Amount2: Optional[X12Nn] = element(
        name="VEH15",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    ActionCode: Optional[X12ID] = element(
        name="VEH16",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="VEH17",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    Name: Optional[X12AN] = element(
        name="VEH18",
        description="Name",
        min_length=1,
        max_length=60,
    )

    CountryCode2: Optional[X12ID] = element(
        name="VEH19",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
