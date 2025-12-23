# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G18(Segment):
    """
    G18 - Store Category Size
    
    Description:
        To identify the shelf size of a department or product category within a retail store
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G18/
    """
    _id: Literal["G18"] = id_element(name="G18")

    EntityIdentifierCode: Optional[X12ID] = element(
        name="G1801",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="G1802",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Length: Optional[X12R] = element(
        name="G1803",
        description="Length",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G1804",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )
