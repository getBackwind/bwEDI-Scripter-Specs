# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class CFI(Segment):
    """
    CFI - Compensation Financial Information
    
    Description:
        To report compensation and or claim financial information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CFI/
    """
    _id: Literal["CFI"] = id_element(name="CFI")

    CodeCategory: X12ID = element(
        name="CFI01",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AdjustmentReasonCode: Optional[X12ID] = element(
        name="CFI02",
        description="Adjustment Reason Code",
        min_length=2,
        max_length=2,
    )

    AdjustmentReasonCodeCharacteristic: Optional[X12ID] = element(
        name="CFI03",
        description="Adjustment Reason Code Characteristic",
        min_length=1,
        max_length=2,
    )

    MaintenanceTypeCode: Optional[X12ID] = element(
        name="CFI04",
        description="Maintenance Type Code",
        min_length=3,
        max_length=3,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="CFI05",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    SettlementTypeCode: Optional[X12ID] = element(
        name="CFI06",
        description="Settlement Type Code",
        min_length=1,
        max_length=1,
    )

    LateReasonCode: Optional[X12ID] = element(
        name="CFI07",
        description="Late Reason Code",
        min_length=2,
        max_length=2,
    )
