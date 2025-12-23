# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class CMC(Segment):
    """
    CMC - Commodity Classification
    
    Description:
        To specify freight commodity code and freight classification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CMC/
    """
    _id: Literal["CMC"] = id_element(name="CMC")

    CommodityCode: Optional[X12AN] = element(
        name="CMC01",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    FreightClassCode: Optional[X12AN] = element(
        name="CMC02",
        description="Freight Class Code",
        min_length=2,
        max_length=5,
    )
