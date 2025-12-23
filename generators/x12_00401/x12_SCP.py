# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SCP(Segment):
    """
    SCP - Beginning Segment for a Cartage Work Assignment Response
    
    Description:
        To indicate the beginning of the Cartage Work Assignment Response Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SCP/
    """
    _id: Literal["SCP"] = id_element(name="SCP")

    StandardCarrierAlphaCode: X12ID = element(
        name="SCP01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ReferenceIdentification: X12AN = element(
        name="SCP02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ReservationActionCode: X12ID = element(
        name="SCP03",
        description="Reservation Action Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ShipmentOrWorkAssignmentDeclineReasonCode: Optional[X12ID] = element(
        name="SCP04",
        description="Shipment or Work Assignment Decline Reason Code",
        min_length=3,
        max_length=3,
    )
