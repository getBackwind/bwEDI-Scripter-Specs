# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class M11(Segment):
    """
    M11 - Manifest Bill of Lading Details
    
    Description:
        To transmit bill of lading detail information for a manifest
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M11/
    """
    _id: Literal["M11"] = id_element(name="M11")

    BillOfLadingWaybillNumber: X12AN = element(
        name="M1101",
        description="Bill of Lading/Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=25,
    )

    LocationIdentifier: X12AN = element(
        name="M1102",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Quantity: Optional[X12R] = element(
        name="M1103",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ManifestUnitCode: Optional[X12ID] = element(
        name="M1104",
        description="Manifest Unit Code",
        min_length=1,
        max_length=3,
    )

    Weight: Optional[X12R] = element(
        name="M1105",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="M1106",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="M1107",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="M1108",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    BillOfLadingTypeCode: Optional[X12ID] = element(
        name="M1109",
        description="Bill of Lading Type Code",
        min_length=2,
        max_length=2,
    )

    PlaceOfReceiptByPreCarrier: Optional[X12AN] = element(
        name="M1110",
        description="Place of Receipt by Pre-carrier",
        min_length=1,
        max_length=17,
    )

    BillOfLadingWaybillNumber2: Optional[X12AN] = element(
        name="M1111",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=25,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="M1112",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="M1113",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="M1114",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode4: Optional[X12ID] = element(
        name="M1115",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ShipperSExportDeclarationRequirements: Optional[X12AN] = element(
        name="M1116",
        description="Shipper's Export Declaration Requirements",
        min_length=1,
        max_length=2,
    )

    ExportExceptionCode: Optional[X12ID] = element(
        name="M1117",
        description="Export Exception Code",
    )

    StandardCarrierAlphaCode5: Optional[X12ID] = element(
        name="M1118",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode6: Optional[X12ID] = element(
        name="M1119",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="M1120",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier3: Optional[X12AN] = element(
        name="M1121",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="M1122",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="M1123",
        description="Payment Method Code",
        min_length=3,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="M1124",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
