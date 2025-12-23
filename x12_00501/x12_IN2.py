# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class IN2(Segment):
    """
    IN2 - Individual Name Structure Components
    
    Description:
        To sequence individual name components for maximum specificity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IN2/
    """
    _id: Literal["IN2"] = id_element(name="IN2")

    NameComponentQualifier: X12ID = element(
        name="IN201",
        description="Name Component Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Name: X12AN = element(
        name="IN202",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    Name2: Optional[X12AN] = element(
        name="IN203",
        description="Name",
        min_length=1,
        max_length=60,
    )
