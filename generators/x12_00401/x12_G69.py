# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class G69(Segment):
    """
    G69 - Line Item Detail - Description
    
    Description:
        To describe an item in free-form format
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G69/
    """
    _id: Literal["G69"] = id_element(name="G69")

    FreeFormDescription: X12AN = element(
        name="G6901",
        description="Free-form Description",
        mandatory=True,
        min_length=1,
        max_length=45,
    )
