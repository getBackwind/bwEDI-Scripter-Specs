# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class TI(Segment):
    """
    TI - Transport Information
    
    Description:
        To identify origin and destination carriers, equipment carrying shipment, date shipped, seal status, and equipment type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TI/
    """
    _id: Literal["TI"] = id_element(name="TI")

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="TI01",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="TI02",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="TI03",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="TI04",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    Date: Optional[X12DT] = element(
        name="TI05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    SealStatusCode: Optional[X12ID] = element(
        name="TI06",
        description="Seal Status Code",
        min_length=2,
        max_length=2,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="TI07",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )
