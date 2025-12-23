# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class X7(Segment):
    """
    X7 - Customs Information
    
    Description:
        To indicate customs information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/X7/
    """
    _id: Literal["X7"] = id_element(name="X7")

    FreeFormMessage: X12AN = element(
        name="X701",
        description="Free-Form Message",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    FreeFormMessage2: Optional[X12AN] = element(
        name="X702",
        description="Free-Form Message",
        min_length=1,
        max_length=30,
    )
