# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G27(Segment):
    """
    G27 - Carrier Detail
    
    Description:
        To specify details of the transportation equipment and carrier routing details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G27/
    """
    _id: Literal["G27"] = id_element(name="G27")

    TransportationMethodTypeCode: X12ID = element(
        name="G2701",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="G2702",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="G2703",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="G2704",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Routing: Optional[X12AN] = element(
        name="G2705",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    ShipmentOrderStatusCode: Optional[X12ID] = element(
        name="G2706",
        description="Shipment/Order Status Code",
        min_length=2,
        max_length=2,
    )
