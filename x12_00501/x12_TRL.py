# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class TRL(Segment):
    """
    TRL - Equipment Usage Information
    
    Description:
        To provide relevant data regarding equipment usage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TRL/
    """
    _id: Literal["TRL"] = id_element(name="TRL")

    EquipmentStatusCode: X12ID = element(
        name="TRL01",
        description="Equipment Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="TRL02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="TRL03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="TRL04",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    RejectReasonCode: Optional[X12ID] = element(
        name="TRL05",
        description="Reject Reason Code",
        min_length=2,
        max_length=2,
    )
