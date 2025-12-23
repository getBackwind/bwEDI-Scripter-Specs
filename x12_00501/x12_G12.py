# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class G12(Segment):
    """
    G12 - Coupon Physical Characteristics
    
    Description:
        To describe physical characteristics and placement of coupons
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G12/
    """
    _id: Literal["G12"] = id_element(name="G12")

    Length: Optional[X12R] = element(
        name="G1201",
        description="Length",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="G1202",
        description="Width",
        min_length=1,
        max_length=8,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="G1203",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="G1204",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PromotionConditionCode: Optional[X12ID] = element(
        name="G1205",
        description="Promotion Condition Code",
        min_length=2,
        max_length=2,
    )

    PositionCode: Optional[X12ID] = element(
        name="G1206",
        description="Position Code",
        min_length=2,
        max_length=2,
    )

    PositionCode2: Optional[X12ID] = element(
        name="G1207",
        description="Position Code",
        min_length=2,
        max_length=2,
    )
