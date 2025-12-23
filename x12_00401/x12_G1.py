# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class G1(Segment):
    """
    G1 - Shipment Type Information
    
    Description:
        To specify the General Commodity (GC) code and any required special indicators for the shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G1/
    """
    _id: Literal["G1"] = id_element(name="G1")

    ShipmentTypeCode: X12ID = element(
        name="G101",
        description="Shipment Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    SpecialIndicatorCode: Optional[X12ID] = element(
        name="G102",
        description="Special Indicator Code",
        min_length=1,
        max_length=1,
    )

    SpecialIndicatorCode2: Optional[X12ID] = element(
        name="G103",
        description="Special Indicator Code",
        min_length=1,
        max_length=1,
    )
