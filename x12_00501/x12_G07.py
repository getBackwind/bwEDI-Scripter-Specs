# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G07(Segment):
    """
    G07 - Carrier Information
    
    Description:
        To identify carrier equipment and condition of shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G07/
    """
    _id: Literal["G07"] = id_element(name="G07")

    EquipmentInitial: Optional[X12AN] = element(
        name="G0701",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="G0702",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    SealNumber: Optional[X12AN] = element(
        name="G0703",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealNumber2: Optional[X12AN] = element(
        name="G0704",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    SealStatusCode: Optional[X12ID] = element(
        name="G0705",
        description="Seal Status Code",
        min_length=2,
        max_length=2,
    )

    Temperature: Optional[X12R] = element(
        name="G0706",
        description="Temperature",
        min_length=1,
        max_length=4,
    )
