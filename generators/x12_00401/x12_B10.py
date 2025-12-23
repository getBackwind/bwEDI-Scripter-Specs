# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class B10(Segment):
    """
    B10 - Beginning Segment for Transportation Carrier Shipment Status Message
    
    Description:
        To transmit identifying numbers and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/B10/
    """
    _id: Literal["B10"] = id_element(name="B10")

    ReferenceIdentification: Optional[X12AN] = element(
        name="B1001",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="B1002",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="B1003",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    InquiryRequestNumber: Optional[X12Nn] = element(
        name="B1004",
        description="Inquiry Request Number",
        min_length=1,
        max_length=3,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="B1005",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="B1006",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="B1007",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
