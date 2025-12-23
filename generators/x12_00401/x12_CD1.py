# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class CD1(Segment):
    """
    CD1 - Cargo Detail
    
    Description:
        To transmit cargo detail information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CD1/
    """
    _id: Literal["CD1"] = id_element(name="CD1")

    EquipmentInitial: X12AN = element(
        name="CD101",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="CD102",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    EquipmentType: Optional[X12ID] = element(
        name="CD103",
        description="Equipment Type",
        min_length=4,
        max_length=4,
    )

    BillOfLadingWaybillNumber: X12AN = element(
        name="CD104",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    TypeOfServiceCode: X12ID = element(
        name="CD105",
        description="Type of Service Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    HazardousMaterialCodeQualifier: Optional[X12ID] = element(
        name="CD106",
        description="Hazardous Material Code Qualifier",
        min_length=1,
        max_length=1,
    )

    HazardousMaterialClassCode: Optional[X12AN] = element(
        name="CD107",
        description="Hazardous Material Class Code",
        min_length=1,
        max_length=4,
    )

    Date: Optional[X12DT] = element(
        name="CD108",
        description="Date",
        min_length=8,
        max_length=8,
    )

    LocationIdentifier: X12AN = element(
        name="CD109",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Quantity: X12R = element(
        name="CD110",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    PackagingCode: X12AN = element(
        name="CD111",
        description="Packaging Code",
        mandatory=True,
        min_length=3,
        max_length=5,
    )

    DispositionCode: X12ID = element(
        name="CD112",
        description="Disposition Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DispositionCode2: Optional[X12ID] = element(
        name="CD113",
        description="Disposition Code",
        min_length=2,
        max_length=2,
    )

    DispositionCode3: Optional[X12ID] = element(
        name="CD114",
        description="Disposition Code",
        min_length=2,
        max_length=2,
    )

    RateClassCode: Optional[X12ID] = element(
        name="CD115",
        description="Rate Class Code",
        min_length=1,
        max_length=3,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="CD116",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Rate: Optional[X12R] = element(
        name="CD117",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    RateClassCode2: Optional[X12ID] = element(
        name="CD118",
        description="Rate Class Code",
        min_length=1,
        max_length=3,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="CD119",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Rate2: Optional[X12R] = element(
        name="CD120",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    RateClassCode3: Optional[X12ID] = element(
        name="CD121",
        description="Rate Class Code",
        min_length=1,
        max_length=3,
    )

    RateValueQualifier3: Optional[X12ID] = element(
        name="CD122",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    Rate3: Optional[X12R] = element(
        name="CD123",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="CD124",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="CD125",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ShipmentStatusCode: Optional[X12ID] = element(
        name="CD126",
        description="Shipment Status Code",
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="CD127",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ReferenceIdentificationQualifier: X12ID = element(
        name="CD128",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="CD129",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier2: X12ID = element(
        name="CD130",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: X12AN = element(
        name="CD131",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )
