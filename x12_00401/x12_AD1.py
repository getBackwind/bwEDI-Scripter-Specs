# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class AD1(Segment):
    """
    AD1 - Adjustment Amount
    
    Description:
        To specify the characteristics of an adjustment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AD1/
    """
    _id: Literal["AD1"] = id_element(name="AD1")

    AdjustmentReasonCode: X12ID = element(
        name="AD101",
        description="Adjustment Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="AD102",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AdjustmentReasonCodeCharacteristic: Optional[X12ID] = element(
        name="AD103",
        description="Adjustment Reason Code Characteristic",
        min_length=1,
        max_length=2,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="AD104",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    LateReasonCode: Optional[X12ID] = element(
        name="AD105",
        description="Late Reason Code",
        min_length=2,
        max_length=2,
    )
