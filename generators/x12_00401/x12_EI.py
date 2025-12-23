# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class EI(Segment):
    """
    EI - Automatic Equipment Identification
    
    Description:
        To identify individual equipment and its sequence number for automatic identification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/EI/
    """
    _id: Literal["EI"] = id_element(name="EI")

    Count: Optional[X12Nn] = element(
        name="EI01",
        description="Count",
        min_length=1,
        max_length=9,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="EI02",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="EI03",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    EquipmentOrientationCode: Optional[X12ID] = element(
        name="EI04",
        description="Equipment Orientation Code",
        min_length=1,
        max_length=1,
    )

    Position: Optional[X12AN] = element(
        name="EI05",
        description="Position",
        min_length=1,
        max_length=3,
    )

    TagStatusCode: Optional[X12ID] = element(
        name="EI06",
        description="Tag Status Code",
        min_length=1,
        max_length=1,
    )
