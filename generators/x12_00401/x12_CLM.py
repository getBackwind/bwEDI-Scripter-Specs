# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CLM(Segment):
    """
    CLM - Health Claim
    
    Description:
        To specify basic data about the claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CLM/
    """
    _id: Literal["CLM"] = id_element(name="CLM")

    ClaimSubmitterSIdentifier: X12AN = element(
        name="CLM01",
        description="Claim Submitter's Identifier",
        mandatory=True,
        min_length=1,
        max_length=38,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CLM02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ClaimFilingIndicatorCode: Optional[X12ID] = element(
        name="CLM03",
        description="Claim Filing Indicator Code",
        min_length=2,
        max_length=2,
    )

    NonInstitutionalClaimTypeCode: Optional[X12ID] = element(
        name="CLM04",
        description="Non-Institutional Claim Type Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CLM06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ProviderAcceptAssignmentCode: Optional[X12ID] = element(
        name="CLM07",
        description="Provider Accept Assignment Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="CLM08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReleaseOfInformationCode: Optional[X12ID] = element(
        name="CLM09",
        description="Release of Information Code",
        min_length=1,
        max_length=1,
    )

    PatientSignatureSourceCode: Optional[X12ID] = element(
        name="CLM10",
        description="Patient Signature Source Code",
        min_length=1,
        max_length=1,
    )

    SpecialProgramCode: Optional[X12ID] = element(
        name="CLM12",
        description="Special Program Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="CLM13",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    LevelOfServiceCode: Optional[X12ID] = element(
        name="CLM14",
        description="Level of Service Code",
        min_length=1,
        max_length=3,
    )

    YesNoConditionOrResponseCode4: Optional[X12ID] = element(
        name="CLM15",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ProviderAgreementCode: Optional[X12ID] = element(
        name="CLM16",
        description="Provider Agreement Code",
        min_length=1,
        max_length=1,
    )

    ClaimStatusCode: Optional[X12ID] = element(
        name="CLM17",
        description="Claim Status Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode5: Optional[X12ID] = element(
        name="CLM18",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ClaimSubmissionReasonCode: Optional[X12ID] = element(
        name="CLM19",
        description="Claim Submission Reason Code",
        min_length=2,
        max_length=2,
    )

    DelayReasonCode: Optional[X12ID] = element(
        name="CLM20",
        description="Delay Reason Code",
        min_length=1,
        max_length=2,
    )
