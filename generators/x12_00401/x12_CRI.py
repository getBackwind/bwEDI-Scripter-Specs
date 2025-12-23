# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CRI(Segment):
    """
    CRI - Claim Report Information
    
    Description:
        To specify information about the claim being reported
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CRI/
    """
    _id: Literal["CRI"] = id_element(name="CRI")

    MaintenanceTypeCode: Optional[X12ID] = element(
        name="CRI01",
        description="Maintenance Type Code",
        min_length=3,
        max_length=3,
    )

    ClaimStatusCode: Optional[X12ID] = element(
        name="CRI02",
        description="Claim Status Code",
        min_length=1,
        max_length=2,
    )

    MaintenanceReasonCode: Optional[X12ID] = element(
        name="CRI03",
        description="Maintenance Reason Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CRI04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="CRI05",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    ClaimFilingIndicatorCode: X12ID = element(
        name="CRI06",
        description="Claim Filing Indicator Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="CRI07",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="CRI08",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    AdjustmentReasonCodeCharacteristic: Optional[X12ID] = element(
        name="CRI09",
        description="Adjustment Reason Code Characteristic",
        min_length=1,
        max_length=2,
    )

    LateReasonCode: Optional[X12ID] = element(
        name="CRI10",
        description="Late Reason Code",
        min_length=2,
        max_length=2,
    )
