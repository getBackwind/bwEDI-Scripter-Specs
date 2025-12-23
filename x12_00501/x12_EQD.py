# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class EQD(Segment):
    """
    EQD - EQD Equipment Damage Information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EQD/
    """
    _id: Literal["EQD"] = id_element(name="EQD")

    DamageLocationOnEquipment: X12ID = element(
        name="EQD01",
        description="Damage Location on Equipment",
        mandatory=True,
    )

    TypeOfDamage: X12ID = element(
        name="EQD02",
        description="Type of Damage",
        mandatory=True,
    )
