# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class DMI(Segment):
    """
    DMI - Data Maintenance Information
    
    Description:
        To provide information related to the data maintenance request number in the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DMI/
    """
    _id: Literal["DMI"] = id_element(name="DMI")

    MaintenanceOperationCode: X12ID = element(
        name="DMI01",
        description="Maintenance Operation Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DataMaintenanceNumber: X12AN = element(
        name="DMI02",
        description="Data Maintenance Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    Name: Optional[X12AN] = element(
        name="DMI03",
        description="Name",
        min_length=1,
        max_length=60,
    )

    AddressInformation: Optional[X12AN] = element(
        name="DMI04",
        description="Address Information",
        min_length=1,
        max_length=55,
    )

    AddressInformation2: Optional[X12AN] = element(
        name="DMI05",
        description="Address Information",
        min_length=1,
        max_length=55,
    )

    CityName: Optional[X12AN] = element(
        name="DMI06",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="DMI07",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    PostalCode: Optional[X12ID] = element(
        name="DMI08",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    CountryCode: Optional[X12ID] = element(
        name="DMI09",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    CommunicationNumberQualifier: Optional[X12ID] = element(
        name="DMI10",
        description="Communication Number Qualifier",
        min_length=2,
        max_length=2,
    )

    CommunicationNumber: Optional[X12AN] = element(
        name="DMI11",
        description="Communication Number",
        min_length=1,
        max_length=256,
    )

    NoteIdentificationNumber: Optional[X12Nn] = element(
        name="DMI12",
        description="Note Identification Number",
        min_length=1,
        max_length=6,
    )
