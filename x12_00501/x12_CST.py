# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class CST(Segment):
    """
    CST - Cost Analysis
    
    Description:
        To provide detailed cost information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CST/
    """
    _id: Literal["CST"] = id_element(name="CST")

    CostCode: X12ID = element(
        name="CST01",
        description="Cost Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="CST02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="CST04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
