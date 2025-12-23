# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class IM(Segment):
    """
    IM - Intermodal Movement Information
    
    Description:
        To specify the overall movement of a shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IM/
    """
    _id: Literal["IM"] = id_element(name="IM")

    WaterMovementCode: Optional[X12ID] = element(
        name="IM01",
        description="Water Movement Code",
        min_length=1,
        max_length=1,
    )

    SpecialHandlingCode: Optional[X12ID] = element(
        name="IM02",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    InlandTransportationCode: Optional[X12ID] = element(
        name="IM03",
        description="Inland Transportation Code",
        min_length=2,
        max_length=2,
    )
