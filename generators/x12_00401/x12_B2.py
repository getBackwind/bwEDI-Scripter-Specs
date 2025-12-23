# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class B2(Segment):
    """
    B2 - Beginning Segment for Shipment Information Transaction
    
    Description:
        To transmit basic data relating to shipment information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/B2/
    """
    _id: Literal["B2"] = id_element(name="B2")

    TariffServiceCode: Optional[X12ID] = element(
        name="B201",
        description="Tariff Service Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="B202",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="B203",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="B204",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="B205",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="B206",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    ShipmentQualifier: Optional[X12ID] = element(
        name="B207",
        description="Shipment Qualifier",
        min_length=1,
        max_length=1,
    )

    TotalEquipment: Optional[X12Nn] = element(
        name="B208",
        description="Total Equipment",
        min_length=1,
        max_length=3,
    )

    ShipmentWeightCode: Optional[X12ID] = element(
        name="B209",
        description="Shipment Weight Code",
        min_length=1,
        max_length=1,
    )

    CustomsDocumentationHandlingCode: Optional[X12ID] = element(
        name="B210",
        description="Customs Documentation Handling Code",
        min_length=2,
        max_length=2,
    )

    TransportationTermsCode: Optional[X12ID] = element(
        name="B211",
        description="Transportation Terms Code",
        min_length=3,
        max_length=3,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="B212",
        description="Payment Method Code",
        min_length=3,
        max_length=3,
    )
