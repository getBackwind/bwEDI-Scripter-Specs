# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SBR(Segment):
    """
    SBR - Subscriber Information
    
    Description:
        To record information specific to the primary insured and the insurance carrier for that insured
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SBR/
    """
    _id: Literal["SBR"] = id_element(name="SBR")

    PayerResponsibilitySequenceNumberCode: X12ID = element(
        name="SBR01",
        description="Payer Responsibility Sequence Number Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    IndividualRelationshipCode: Optional[X12ID] = element(
        name="SBR02",
        description="Individual Relationship Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="SBR03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Name: Optional[X12AN] = element(
        name="SBR04",
        description="Name",
        min_length=1,
        max_length=60,
    )

    InsuranceTypeCode: Optional[X12ID] = element(
        name="SBR05",
        description="Insurance Type Code",
        min_length=1,
        max_length=2,
    )

    CoordinationOfBenefitsCode: Optional[X12ID] = element(
        name="SBR06",
        description="Coordination of Benefits Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SBR07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    EmploymentStatusCode: Optional[X12ID] = element(
        name="SBR08",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    ClaimFilingIndicatorCode: Optional[X12ID] = element(
        name="SBR09",
        description="Claim Filing Indicator Code",
        min_length=2,
        max_length=2,
    )
