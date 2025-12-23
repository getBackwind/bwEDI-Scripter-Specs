# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class G73(Segment):
    """
    G73 - Allowance or Charge Description
    
    Description:
        To describe the allowance or charge in free-form format
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G73/
    """
    _id: Literal["G73"] = id_element(name="G73")

    FreeFormDescription: X12AN = element(
        name="G7301",
        description="Free-form Description",
        mandatory=True,
        min_length=1,
        max_length=45,
    )
