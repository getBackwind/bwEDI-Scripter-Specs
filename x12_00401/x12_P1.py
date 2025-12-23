# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12TM


class P1(Segment):
    """
    P1 - Pick-up
    
    Description:
        To specify the pick-up details including time, date, and equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/P1/
    """
    _id: Literal["P1"] = id_element(name="P1")

    PickUpOrDeliveryCode: Optional[X12ID] = element(
        name="P101",
        description="Pick-up or Delivery Code",
    )

    PickUpDate: X12DT = element(
        name="P102",
        description="Pick-up Date",
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

    PickUpTime: Optional[X12TM] = element(
        name="P104",
        description="Pick-up Time",
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
        max_length=10,
    )

    NumberOfShipments: Optional[X12Nn] = element(
        name="P107",
        description="Number of Shipments",
        min_length=1,
        max_length=5,
    )
