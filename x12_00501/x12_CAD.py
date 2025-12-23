# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CAD(Segment):
    """
    CAD - Carrier Details
    
    Description:
        To specify transportation details for the transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CAD/
    """
    _id: Literal["CAD"] = id_element(name="CAD")

    TransportationMethod: X12ID = element(
        name="CAD01",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="CAD02",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="CAD03",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    AlphaCode: Optional[X12ID] = element(
        name="CAD04",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Routing: Optional[X12AN] = element(
        name="CAD05",
        description="Routing",
        min_length=1,
        max_length=35,
    )

    ShipmentOrderStatusCode: Optional[X12ID] = element(
        name="CAD06",
        description="Shipment/Order Status Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdQualifier: Optional[X12ID] = element(
        name="CAD07",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceID: Optional[X12AN] = element(
        name="CAD08",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ServiceLevelCode: Optional[X12ID] = element(
        name="CAD09",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )
