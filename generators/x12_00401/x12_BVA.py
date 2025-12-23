# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class BVA(Segment):
    """
    BVA - Beginning Vehicle Advice
    
    Description:
        To indicate the beginning of the Vehicle Application Advice Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BVA/
    """
    _id: Literal["BVA"] = id_element(name="BVA")

    PaymentTypeCode: X12ID = element(
        name="BVA01",
        description="Payment Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="BVA02",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="BVA03",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="BVA04",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    Date: X12DT = element(
        name="BVA05",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="BVA06",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="BVA07",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="BVA08",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    VehicleServiceCode: Optional[X12ID] = element(
        name="BVA09",
        description="Vehicle Service Code",
        min_length=2,
        max_length=2,
    )

    IdentificationCodeQualifier3: Optional[X12ID] = element(
        name="BVA10",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode3: Optional[X12AN] = element(
        name="BVA11",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="BVA12",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )

    LadingDescriptionQualifier: Optional[X12ID] = element(
        name="BVA13",
        description="Lading Description Qualifier",
        min_length=1,
        max_length=1,
    )

    Date2: Optional[X12DT] = element(
        name="BVA14",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BVA15",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Date3: Optional[X12DT] = element(
        name="BVA16",
        description="Date",
        min_length=8,
        max_length=8,
    )

    CheckNumber: Optional[X12AN] = element(
        name="BVA17",
        description="Check Number",
        min_length=1,
        max_length=16,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="BVA18",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="BVA19",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="BVA20",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="BVA21",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="BVA22",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    FlightVoyageNumber: Optional[X12AN] = element(
        name="BVA23",
        description="Flight/Voyage Number",
        min_length=2,
        max_length=10,
    )

    VehicleStatus: Optional[X12AN] = element(
        name="BVA24",
        description="Vehicle Status",
        min_length=1,
        max_length=2,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BVA25",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )
