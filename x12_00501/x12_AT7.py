# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12TM


class AT7(Segment):
    """
    AT7 - Shipment Status Details
    
    Description:
        To specify the status of a shipment, the reason for that status, the date and time of the status and the date and time of any appointments scheduled.
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AT7/
    """
    _id: Literal["AT7"] = id_element(name="AT7")

    ShipmentStatusIndicator: Optional[X12ID] = element(
        name="AT701",
        description="Shipment Status Indicator",
    )

    ShipmentStatusOrAppointmentReasonCode: Optional[X12ID] = element(
        name="AT702",
        description="Shipment Status or Appointment Reason Code",
        min_length=2,
        max_length=2,
    )

    ShipmentAppointmentStatusCode: Optional[X12ID] = element(
        name="AT703",
        description="Shipment Appointment Status Code",
        min_length=2,
        max_length=2,
    )

    ShipmentStatusOrAppointmentReasonCode2: Optional[X12ID] = element(
        name="AT704",
        description="Shipment Status or Appointment Reason Code",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="AT705",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="AT706",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="AT707",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
