# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DMA(Segment):
    """
    DMA - Additional Demographic Information
    
    Description:
        To supply additional demographic identification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DMA/
    """
    _id: Literal["DMA"] = id_element(name="DMA")

    ReferenceIdentification: Optional[X12AN] = element(
        name="DMA01",
        description="Reference Identification",
        min_length=1,
        max_length=50,
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
        max_length=50,
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

    CodeForLicensingCertificationRegistrationOrAccreditationAgency: Optional[X12ID] = element(
        name="DMA06",
        description="Code For Licensing, Certification, Registration, or Accreditation Agency",
        min_length=1,
        max_length=2,
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

    CityName: Optional[X12AN] = element(
        name="DMA10",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    Color: Optional[X12AN] = element(
        name="DMA11",
        description="Color",
        min_length=1,
        max_length=10,
    )

    Color2: Optional[X12AN] = element(
        name="DMA12",
        description="Color",
        min_length=1,
        max_length=10,
    )

    MeasurementUnitQualifier: Optional[X12ID] = element(
        name="DMA13",
        description="Measurement Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Height: Optional[X12R] = element(
        name="DMA14",
        description="Height",
        min_length=1,
        max_length=8,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="DMA15",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="DMA16",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Description: Optional[X12AN] = element(
        name="DMA17",
        description="Description",
        min_length=1,
        max_length=80,
    )

    CountryCode2: Optional[X12ID] = element(
        name="DMA18",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
