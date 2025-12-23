# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class R2D(Segment):
    """
    R2D - Miscellaneous Charge
    
    Description:
        To identify miscellaneous charge detail for carriers participating in the route
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R2D/
    """
    _id: Literal["R2D"] = id_element(name="R2D")

    SpecialChargeOrAllowanceCode: X12ID = element(
        name="R2D01",
        description="Special Charge or Allowance Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Amount: X12Nn = element(
        name="R2D02",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )
