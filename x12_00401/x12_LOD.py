# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LOD(Segment):
    """
    LOD - Location Description
    
    Description:
        To provide a general description of the area where an entity is located
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LOD/
    """
    _id: Literal["LOD"] = id_element(name="LOD")

    GeneralTerritoryCode: Optional[X12ID] = element(
        name="LOD01",
        description="General Territory Code",
        min_length=1,
        max_length=1,
    )

    ConditionIndicator: Optional[X12ID] = element(
        name="LOD02",
        description="Condition Indicator",
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="LOD03",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )

    ThoroughfareTypeQualifier: Optional[X12ID] = element(
        name="LOD04",
        description="Thoroughfare Type Qualifier",
        min_length=1,
        max_length=1,
    )

    ThoroughfareTypeCode: Optional[X12ID] = element(
        name="LOD05",
        description="Thoroughfare Type Code",
        min_length=1,
        max_length=1,
    )

    FreeFormMessage2: Optional[X12AN] = element(
        name="LOD06",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )
