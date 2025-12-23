# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class UM(Segment):
    """
    UM - Health Care Services Review Information
    
    Description:
        To specify health care services review information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/UM/
    """
    _id: Literal["UM"] = id_element(name="UM")

    RequestCategoryCode: X12ID = element(
        name="UM01",
        description="Request Category Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CertificationTypeCode: Optional[X12ID] = element(
        name="UM02",
        description="Certification Type Code",
        min_length=1,
        max_length=1,
    )

    ServiceTypeCode: Optional[X12ID] = element(
        name="UM03",
        description="Service Type Code",
        min_length=1,
        max_length=2,
    )

    FacilityCodeValue: X12AN = element(
        name="UM0401",
        description="Facility Code Value",
        mandatory=True,
        min_length=0,
        max_length=2,
    )

    FacilityCodeQualifier: Optional[X12ID] = element(
        name="UM0402",
        description="Facility Code Qualifier",
        min_length=1,
        max_length=1,
    )

    ClaimFrequencyTypeCode: Optional[X12ID] = element(
        name="UM0403",
        description="Claim Frequency Type Code",
        min_length=1,
        max_length=1,
    )

    RelatedCausesCode: X12ID = element(
        name="UM0501",
        description="Related-Causes Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RelatedCausesCode2: Optional[X12ID] = element(
        name="UM0502",
        description="Related-Causes Code",
        min_length=2,
        max_length=2,
    )

    RelatedCausesCode3: Optional[X12ID] = element(
        name="UM0503",
        description="Related-Causes Code",
        min_length=2,
        max_length=2,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="UM0504",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="UM0505",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    LevelOfServiceCode: Optional[X12ID] = element(
        name="UM06",
        description="Level of Service Code",
        min_length=1,
        max_length=3,
    )

    CurrentHealthConditionCode: Optional[X12ID] = element(
        name="UM07",
        description="Current Health Condition Code",
        min_length=1,
        max_length=1,
    )

    PrognosisCode: Optional[X12ID] = element(
        name="UM08",
        description="Prognosis Code",
        min_length=1,
        max_length=1,
    )

    ReleaseOfInformationCode: Optional[X12ID] = element(
        name="UM09",
        description="Release of Information Code",
        min_length=1,
        max_length=1,
    )

    DelayReasonCode: Optional[X12ID] = element(
        name="UM10",
        description="Delay Reason Code",
        min_length=1,
        max_length=2,
    )
