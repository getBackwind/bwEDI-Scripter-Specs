# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class HL(Segment):
    """
    HL - Hierarchical Level
    
    Description:
        To identify dependencies among and the content of hierarchically related groups of data segments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/HL/
    """
    _id: Literal["HL"] = id_element(name="HL")

    HierarchicalID: X12AN = element(
        name="HL01",
        description="Hierarchical ID Number",
        mandatory=True,
        min_length=1,
        max_length=12,
    )

    ParentID: Optional[X12AN] = element(
        name="HL02",
        description="Hierarchical Parent ID Number",
        min_length=1,
        max_length=12,
    )

    HierarchicalLevel: X12ID = element(
        name="HL03",
        description="Hierarchical Level Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    HierarchicalChildCode: Optional[X12ID] = element(
        name="HL04",
        description="Hierarchical Child Code",
        min_length=1,
        max_length=1,
    )
