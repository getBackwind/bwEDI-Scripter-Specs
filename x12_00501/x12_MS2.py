# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class MS2(Segment):
    """
    MS2 - Equipment or Container Owner and Type
    
    Description:
        To specify the owner, the identification number assigned by that owner, and the type of equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MS2/
    """
    _id: Literal["MS2"] = id_element(name="MS2")

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="MS201",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="MS202",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="MS203",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    EquipmentNumberCheckDigit: Optional[X12Nn] = element(
        name="MS204",
        description="Equipment Number Check Digit",
        min_length=1,
        max_length=1,
    )
