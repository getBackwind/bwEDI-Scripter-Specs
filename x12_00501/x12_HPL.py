# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class HPL(Segment):
    """
    HPL - Health Care Provider License
    
    Description:
        To provide license, certification, accreditation, and registration information for health care providers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/HPL/
    """
    _id: Literal["HPL"] = id_element(name="HPL")

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="HPL01",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="HPL02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    StatusCode: Optional[X12ID] = element(
        name="HPL03",
        description="Status Code",
        min_length=2,
        max_length=2,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="HPL04",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="HPL05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    CodeForLicensingCertificationRegistrationOrAccreditationAgency: Optional[X12ID] = element(
        name="HPL06",
        description="Code For Licensing, Certification, Registration, or Accreditation Agency",
        min_length=1,
        max_length=2,
    )
