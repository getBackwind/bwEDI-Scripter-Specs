# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CQ(Segment):
    """
    CQ - Credentials and Qualifications
    
    Description:
        To provide information on any certificate, license, permit, credential, or qualification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CQ/
    """
    _id: Literal["CQ"] = id_element(name="CQ")

    CredentialTypeCode: X12ID = element(
        name="CQ01",
        description="Credential Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CredentialCategoryCode: Optional[X12ID] = element(
        name="CQ02",
        description="Credential Category Code",
        min_length=1,
        max_length=2,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="CQ03",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="CQ04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    LevelOfIndividualTestOrCourseCode: Optional[X12ID] = element(
        name="CQ05",
        description="Level of Individual, Test, or Course Code",
        min_length=2,
        max_length=2,
    )

    BasisForAcademicCreditOrAwardOfCredentialCode: Optional[X12ID] = element(
        name="CQ06",
        description="Basis for Academic Credit or Award of Credential Code",
        min_length=1,
        max_length=1,
    )

    CredentialRequirementCode: Optional[X12ID] = element(
        name="CQ07",
        description="Credential Requirement Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="CQ08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ConditionIndicator: Optional[X12ID] = element(
        name="CQ09",
        description="Condition Indicator",
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="CQ10",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
