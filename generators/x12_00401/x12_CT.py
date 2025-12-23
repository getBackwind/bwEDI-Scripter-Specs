# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class CT(Segment):
    """
    CT - Car Type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CT/
    """
    _id: Literal["CT"] = id_element(name="CT")

    YesNoConditionOrResponseCode: X12ID = element(
        name="CT01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CarTypeCode: X12ID = element(
        name="CT02",
        description="Car Type Code",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    CarTypeCode2: Optional[X12ID] = element(
        name="CT03",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )
