# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SLA(Segment):
    """
    SLA - School Accreditation and Licensing
    
    Description:
        To provide educational institution accreditation, affiliation, and licensing information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SLA/
    """
    _id: Literal["SLA"] = id_element(name="SLA")

    CodeListQualifierCode: X12ID = element(
        name="SLA01",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="SLA02",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    CodeForLicensingCertificationRegistrationOrAccreditationAgency: Optional[X12ID] = element(
        name="SLA03",
        description="Code For Licensing, Certification, Registration, or Accreditation Agency",
        min_length=1,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="SLA04",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="SLA05",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    CodeListQualifierCode2: Optional[X12ID] = element(
        name="SLA06",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="SLA07",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="SLA08",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
