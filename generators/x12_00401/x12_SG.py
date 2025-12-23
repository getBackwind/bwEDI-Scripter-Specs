# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12TM


class SG(Segment):
    """
    SG - Shipment Status
    
    Description:
        To convey the status of a shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SG/
    """
    _id: Literal["SG"] = id_element(name="SG")

    ShipmentStatusCode: Optional[X12ID] = element(
        name="SG01",
        description="Shipment Status Code",
        min_length=1,
        max_length=2,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="SG02",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    DispositionCode: Optional[X12ID] = element(
        name="SG03",
        description="Disposition Code",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="SG04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="SG05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="SG06",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
