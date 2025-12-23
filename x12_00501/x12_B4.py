# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12TM


class B4(Segment):
    """
    B4 - Beginning Segment for Inquiry or Reply
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/B4/
    """
    _id: Literal["B4"] = id_element(name="B4")

    SpecialHandlingCode: Optional[X12ID] = element(
        name="B401",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    InquiryRequestNumber: Optional[X12Nn] = element(
        name="B402",
        description="Inquiry Request Number",
        min_length=1,
        max_length=3,
    )

    ShipmentStatusCode: Optional[X12ID] = element(
        name="B403",
        description="Shipment Status Code",
        min_length=1,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="B404",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="B405",
        description="Time",
        min_length=4,
        max_length=8,
    )

    StatusLocation: Optional[X12AN] = element(
        name="B406",
        description="Status Location",
        min_length=3,
        max_length=5,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="B407",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="B408",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    EquipmentStatusCode: Optional[X12ID] = element(
        name="B409",
        description="Equipment Status Code",
        min_length=1,
        max_length=2,
    )

    EquipmentType: Optional[X12ID] = element(
        name="B410",
        description="Equipment Type",
        min_length=4,
        max_length=4,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="B411",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="B412",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    EquipmentNumberCheckDigit: Optional[X12Nn] = element(
        name="B413",
        description="Equipment Number Check Digit",
        min_length=1,
        max_length=1,
    )
