# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class B12(Segment):
    """
    B12 - Beginning Segment for Consolidation of Goods In Container
    
    Description:
        To specify the beginning of the Consolidation of Goods in Container Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/B12/
    """
    _id: Literal["B12"] = id_element(name="B12")

    EquipmentInitial: X12AN = element(
        name="B1201",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="B1202",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    EquipmentType: X12ID = element(
        name="B1203",
        description="Equipment Type",
        mandatory=True,
        min_length=4,
        max_length=4,
    )
