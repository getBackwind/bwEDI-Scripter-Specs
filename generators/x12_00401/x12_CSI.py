# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CSI(Segment):
    """
    CSI - Claim Status Information
    
    Description:
        To indicate the status of a claim for mortgage insurance benefits
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CSI/
    """
    _id: Literal["CSI"] = id_element(name="CSI")

    ClaimSubmissionReasonCode: X12ID = element(
        name="CSI01",
        description="Claim Submission Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: X12ID = element(
        name="CSI02",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="CSI03",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="CSI04",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )
