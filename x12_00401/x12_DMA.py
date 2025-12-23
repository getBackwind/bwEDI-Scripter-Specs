# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class DMA(Segment):
    """
    DMA - Additional Demographic Information
    
    Description:
        To supply additional demographic identification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DMA/
    """
    _id: Literal["DMA"] = id_element(name="DMA")

    ReferenceIdentification: Optional[X12AN] = element(
        name="DMA01",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="DMA02",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="DMA03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="DMA04",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    ApplicantTypeCode: Optional[X12ID] = element(
        name="DMA05",
        description="Applicant Type Code",
        min_length=1,
        max_length=1,
    )

    LicensingAgencyCode: Optional[X12ID] = element(
        name="DMA06",
        description="Licensing Agency Code",
    )

    CountryCode: Optional[X12ID] = element(
        name="DMA07",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    LanguageCode: Optional[X12ID] = element(
        name="DMA08",
        description="Language Code",
        min_length=2,
        max_length=3,
    )

    StatusCode: Optional[X12ID] = element(
        name="DMA09",
        description="Status Code",
        min_length=2,
        max_length=2,
    )
