# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class G15(Segment):
    """
    G15 - Coupon Distribution
    
    Description:
        To specify the number of coupons and method of circulation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G15/
    """
    _id: Literal["G15"] = id_element(name="G15")

    Quantity: X12R = element(
        name="G1501",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    CouponDistributionMediaCode: X12ID = element(
        name="G1502",
        description="Coupon Distribution Media Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CouponTypeCode: Optional[X12ID] = element(
        name="G1503",
        description="Coupon Type Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="G1504",
        description="Description",
        min_length=1,
        max_length=80,
    )
