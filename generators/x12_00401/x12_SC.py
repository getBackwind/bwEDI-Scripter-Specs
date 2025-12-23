# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn


class SC(Segment):
    """
    SC - Docket Sub-level
    
    Description:
        To indicate the docket sub-level
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SC/
    """
    _id: Literal["SC"] = id_element(name="SC")

    Level: X12Nn = element(
        name="SC01",
        description="Level",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    SubLevel: X12AN = element(
        name="SC02",
        description="Sub Level",
        mandatory=True,
        min_length=1,
        max_length=3,
    )
