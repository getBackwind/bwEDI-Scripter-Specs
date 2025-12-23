# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G94(Segment):
    """
    G94 - Promotion Conditions
    
    Description:
        To indicate the option number associated with a promotion and to specify the "AND"or "OR"condition for the option
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G94/
    """
    _id: Literal["G94"] = id_element(name="G94")

    PromotionConditionQualifier: Optional[X12ID] = element(
        name="G9401",
        description="Promotion Condition Qualifier",
        min_length=2,
        max_length=2,
    )

    OptionNumber: X12AN = element(
        name="G9402",
        description="Option Number",
        mandatory=True,
        min_length=1,
        max_length=20,
    )
