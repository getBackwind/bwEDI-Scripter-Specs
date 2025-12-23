# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BW(Segment):
    """
    BW - Beginning Segment for Weight Message Set
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BW/
    """
    _id: Literal["BW"] = id_element(name="BW")

    OriginEDICarrierCode: X12ID = element(
        name="BW01",
        description="Origin EDI Carrier Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="BW02",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    WeightUnitCode: X12ID = element(
        name="BW03",
        description="Weight Unit Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
