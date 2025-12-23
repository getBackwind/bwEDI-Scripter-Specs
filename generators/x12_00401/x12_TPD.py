# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TPD(Segment):
    """
    TPD - Trading Partner Detail
    
    Description:
        To describe attribute of a trading partner
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TPD/
    """
    _id: Literal["TPD"] = id_element(name="TPD")

    ItemDescriptionType: X12ID = element(
        name="TPD01",
        description="Item Description Type",
        mandatory=True,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="TPD02",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="TPD03",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="TPD04",
        description="Description",
        min_length=1,
        max_length=80,
    )
