# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class G36(Segment):
    """
    G36 - Price List Reference
    
    Description:
        To provide price list references and descriptions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G36/
    """
    _id: Literal["G36"] = id_element(name="G36")

    PriceListNumber: X12AN = element(
        name="G3601",
        description="Price List Number",
        mandatory=True,
        min_length=1,
        max_length=16,
    )

    PriceListIssueNumber: Optional[X12AN] = element(
        name="G3602",
        description="Price List Issue Number",
        min_length=1,
        max_length=16,
    )

    Date: X12DT = element(
        name="G3603",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    PriceConditionAppliesCode: Optional[X12ID] = element(
        name="G3604",
        description="Price Condition Applies Code",
        min_length=3,
        max_length=3,
    )
