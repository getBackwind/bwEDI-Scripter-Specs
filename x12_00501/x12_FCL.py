# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class FCL(Segment):
    """
    FCL - Foreclosure
    
    Description:
        To specify legal outcome and impact of foreclosure on a lender's claim for mortgage insurance benefits
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FCL/
    """
    _id: Literal["FCL"] = id_element(name="FCL")

    DeficiencyJudgmentCode: Optional[X12ID] = element(
        name="FCL01",
        description="Deficiency Judgment Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="FCL02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="FCL03",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="FCL04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AdjustmentReasonCode: Optional[X12ID] = element(
        name="FCL05",
        description="Adjustment Reason Code",
        min_length=2,
        max_length=2,
    )
