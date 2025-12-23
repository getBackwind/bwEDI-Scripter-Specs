# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CIC(Segment):
    """
    CIC - Car Information Control
    
    Description:
        To transmit identifying equipment mark and type associated with the cycle or transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CIC/
    """
    _id: Literal["CIC"] = id_element(name="CIC")

    EquipmentInitial: Optional[X12AN] = element(
        name="CIC01",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="CIC02",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="CIC03",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber2: Optional[X12AN] = element(
        name="CIC04",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    MechanicalCarCode: Optional[X12ID] = element(
        name="CIC05",
        description="Mechanical Car Code",
        min_length=4,
        max_length=4,
    )
