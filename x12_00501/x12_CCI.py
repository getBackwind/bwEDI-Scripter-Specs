# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CCI(Segment):
    """
    CCI - Credit Counseling Information
    
    Description:
        To define the applicant's participation in credit counseling
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CCI/
    """
    _id: Literal["CCI"] = id_element(name="CCI")

    IdentificationCode: X12AN = element(
        name="CCI01",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    ReferenceIdentification: X12AN = element(
        name="CCI02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="CCI03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="CCI04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="CCI05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="CCI06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="CCI07",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="CCI08",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="CCI09",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    CounselingStatusCode: Optional[X12ID] = element(
        name="CCI10",
        description="Counseling Status Code",
        min_length=1,
        max_length=1,
    )
