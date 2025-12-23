# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class L9(Segment):
    """
    L9 - Charge Detail
    
    Description:
        To specify special charge code and the associated monetary amount
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/L9/
    """
    _id: Literal["L9"] = id_element(name="L9")

    SpecialChargeOrAllowanceCode: X12ID = element(
        name="L901",
        description="Special Charge or Allowance Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="L902",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )
