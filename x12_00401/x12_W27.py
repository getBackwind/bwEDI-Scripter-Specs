# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class W27(Segment):
    """
    W27 - Carrier Detail
    
    Description:
        To specify details of the transportation equipment and carrier routing details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W27/
    """
    _id: Literal["W27"] = id_element(name="W27")

    TransportationMethodTypeCode: X12ID = element(
        name="W2701",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="W2702",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Routing: Optional[X12AN] = element(
        name="W2703",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    ShipmentMethodOfPayment: Optional[X12ID] = element(
        name="W2704",
        description="Shipment Method of Payment",
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="W2705",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="W2706",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="W2707",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    ShipmentOrderStatusCode: Optional[X12ID] = element(
        name="W2708",
        description="Shipment/Order Status Code",
        min_length=2,
        max_length=2,
    )

    SpecialHandlingCode: Optional[X12ID] = element(
        name="W2709",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    CarrierRouteChangeReasonCode: Optional[X12ID] = element(
        name="W2710",
        description="Carrier/Route Change Reason Code",
        min_length=2,
        max_length=2,
    )
