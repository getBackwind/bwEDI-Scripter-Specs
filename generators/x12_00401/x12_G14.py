# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class G14(Segment):
    """
    G14 - Coupon Special Processing
    
    Description:
        To describe special processing associated with coupons
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G14/
    """
    _id: Literal["G14"] = id_element(name="G14")

    ServicePromotionAllowanceOrChargeCode: X12ID = element(
        name="G1401",
        description="Service, Promotion, Allowance, or Charge Code",
        mandatory=True,
    )

    ServicePromotionAllowanceOrChargeCode2: Optional[X12ID] = element(
        name="G1402",
        description="Service, Promotion, Allowance, or Charge Code",
    )
