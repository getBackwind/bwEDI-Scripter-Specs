# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class H3(Segment):
    """
    H3 - Special Handling Instructions
    
    Description:
        To specify special handling instructions in coded or free-form format
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/H3/
    """
    _id: Literal["H3"] = id_element(name="H3")

    SpecialHandlingCode: Optional[X12ID] = element(
        name="H301",
        description="Special Handling Code",
        min_length=2,
        max_length=3,
    )

    SpecialHandlingDescription: Optional[X12AN] = element(
        name="H302",
        description="Special Handling Description",
        min_length=2,
        max_length=30,
    )

    ProtectiveServiceCode: Optional[X12ID] = element(
        name="H303",
        description="Protective Service Code",
        min_length=1,
        max_length=3,
    )

    VentInstructionCode: Optional[X12ID] = element(
        name="H304",
        description="Vent Instruction Code",
        min_length=2,
        max_length=3,
    )

    TariffApplicationCode: Optional[X12ID] = element(
        name="H305",
        description="Tariff Application Code",
        min_length=1,
        max_length=1,
    )
