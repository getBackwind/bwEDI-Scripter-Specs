# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12TM


class P1(Segment):
    """
    P1 - Pickup
    
    Description:
        To specify the pickup details including time, date, and equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/P1/
    """
    _id: Literal["P1"] = id_element(name="P1")

    PickupOrDeliveryCode: Optional[X12ID] = element(
        name="P101",
        description="Pickup or Delivery Code",
        min_length=1,
        max_length=2,
    )

    PickupDate: X12DT = element(
        name="P102",
        description="Pickup Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier: X12ID = element(
        name="P103",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    PickupTime: Optional[X12TM] = element(
        name="P104",
        description="Pickup Time",
        min_length=4,
        max_length=4,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="P105",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="P106",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    NumberOfShipments: Optional[X12Nn] = element(
        name="P107",
        description="Number of Shipments",
        min_length=1,
        max_length=5,
    )
