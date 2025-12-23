# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class G35(Segment):
    """
    G35 - Advertising Feature Information
    
    Description:
        To specify advertising type and coupon information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G35/
    """
    _id: Literal["G35"] = id_element(name="G35")

    PromotionConditionCode: Optional[X12ID] = element(
        name="G3501",
        description="Promotion Condition Code",
        min_length=2,
        max_length=2,
    )

    CouponTypeCode: Optional[X12ID] = element(
        name="G3502",
        description="Coupon Type Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="G3503",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
