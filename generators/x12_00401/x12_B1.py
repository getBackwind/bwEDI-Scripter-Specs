# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class B1(Segment):
    """
    B1 - Beginning Segment for Booking or Pick-up/Delivery
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/B1/
    """
    _id: Literal["B1"] = id_element(name="B1")

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="B101",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ShipmentIdentificationNumber: X12AN = element(
        name="B102",
        description="Shipment Identification Number",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="B103",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReservationActionCode: Optional[X12ID] = element(
        name="B104",
        description="Reservation Action Code",
        min_length=1,
        max_length=1,
    )
