# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class G24(Segment):
    """
    G24 - Promotion Reference
    
    Description:
        To reference a promotion number related to the price change
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G24/
    """
    _id: Literal["G24"] = id_element(name="G24")

    AllowanceOrChargeNumber: X12AN = element(
        name="G2401",
        description="Allowance or Charge Number",
        mandatory=True,
        min_length=1,
        max_length=16,
    )
