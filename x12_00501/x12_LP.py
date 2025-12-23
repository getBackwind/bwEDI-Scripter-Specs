# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class LP(Segment):
    """
    LP - Load Planning
    
    Description:
        To describe information for loading aircraft with vehicles and other items
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LP/
    """
    _id: Literal["LP"] = id_element(name="LP")

    EquipmentType: Optional[X12ID] = element(
        name="LP01",
        description="Equipment Type",
        min_length=4,
        max_length=4,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="LP02",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    ShipmentIdentificationNumber2: Optional[X12AN] = element(
        name="LP03",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    VentInstructionCode: Optional[X12ID] = element(
        name="LP04",
        description="Vent Instruction Code",
        min_length=2,
        max_length=3,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="LP05",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    Number: Optional[X12Nn] = element(
        name="LP06",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="LP07",
        description="Number",
        min_length=1,
        max_length=9,
    )
