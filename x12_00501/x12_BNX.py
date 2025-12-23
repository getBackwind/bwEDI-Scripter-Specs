# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class BNX(Segment):
    """
    BNX - Rail Shipment Information
    
    Description:
        To transmit rail-specific shipment data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BNX/
    """
    _id: Literal["BNX"] = id_element(name="BNX")

    ShipmentWeightCode: Optional[X12ID] = element(
        name="BNX01",
        description="Shipment Weight Code",
        min_length=1,
        max_length=1,
    )

    ReferencedPatternIdentifier: Optional[X12AN] = element(
        name="BNX02",
        description="Referenced Pattern Identifier",
        min_length=1,
        max_length=13,
    )

    BillingCode: Optional[X12ID] = element(
        name="BNX03",
        description="Billing Code",
        min_length=1,
        max_length=1,
    )

    RepetitivePatternNumber: Optional[X12Nn] = element(
        name="BNX04",
        description="Repetitive Pattern Number",
        min_length=5,
        max_length=5,
    )
