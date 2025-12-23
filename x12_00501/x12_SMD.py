# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class SMD(Segment):
    """
    SMD - Consolidated Shipment Manifest Data
    
    Description:
        To transmit shipment manifest data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SMD/
    """
    _id: Literal["SMD"] = id_element(name="SMD")

    ServiceLevelCode: X12ID = element(
        name="SMD01",
        description="Service Level Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ShipmentMethodOfPayment: X12ID = element(
        name="SMD02",
        description="Shipment Method of Payment",
        mandatory=True,
    )

    PickupOrDeliveryCode: Optional[X12ID] = element(
        name="SMD03",
        description="Pickup or Delivery Code",
        min_length=1,
        max_length=2,
    )
