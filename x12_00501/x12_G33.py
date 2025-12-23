# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class G33(Segment):
    """
    G33 - Total Dollars Summary
    
    Description:
        To specify the total invoice amount, including charges less allowances, before terms discount
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G33/
    """
    _id: Literal["G33"] = id_element(name="G33")

    Amount: X12Nn = element(
        name="G3301",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )
