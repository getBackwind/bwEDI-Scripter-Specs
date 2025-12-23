# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class DFI(Segment):
    """
    DFI - Default Information
    
    Description:
        To specify mortgage loan default information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DFI/
    """
    _id: Literal["DFI"] = id_element(name="DFI")

    StatusReasonCode: Optional[X12ID] = element(
        name="DFI01",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    ClaimFilingIndicatorCode: Optional[X12ID] = element(
        name="DFI02",
        description="Claim Filing Indicator Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="DFI03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="DFI04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
