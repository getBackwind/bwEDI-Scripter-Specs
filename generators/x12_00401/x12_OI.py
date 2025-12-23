# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class OI(Segment):
    """
    OI - Other Health Insurance Information
    
    Description:
        To specify information associated with other health insurance coverage
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/OI/
    """
    _id: Literal["OI"] = id_element(name="OI")

    ClaimFilingIndicatorCode: Optional[X12ID] = element(
        name="OI01",
        description="Claim Filing Indicator Code",
        min_length=2,
        max_length=2,
    )

    ClaimSubmissionReasonCode: Optional[X12ID] = element(
        name="OI02",
        description="Claim Submission Reason Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="OI03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    PatientSignatureSourceCode: Optional[X12ID] = element(
        name="OI04",
        description="Patient Signature Source Code",
        min_length=1,
        max_length=1,
    )

    ProviderAgreementCode: Optional[X12ID] = element(
        name="OI05",
        description="Provider Agreement Code",
        min_length=1,
        max_length=1,
    )

    ReleaseOfInformationCode: Optional[X12ID] = element(
        name="OI06",
        description="Release of Information Code",
        min_length=1,
        max_length=1,
    )
