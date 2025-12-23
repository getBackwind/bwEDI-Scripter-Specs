# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class INX(Segment):
    """
    INX - Index Detail
    
    Description:
        To specify an index
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/INX/
    """
    _id: Literal["INX"] = id_element(name="INX")

    IndexQualifier: X12ID = element(
        name="INX01",
        description="Index Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
