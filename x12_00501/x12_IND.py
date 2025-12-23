# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class IND(Segment):
    """
    IND - Additional Individual Demographic Information
    
    Description:
        To provide additional demographic information to the receiving school, institution, or agency to assist in identifying the particular student
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IND/
    """
    _id: Literal["IND"] = id_element(name="IND")

    CountryCode: Optional[X12ID] = element(
        name="IND01",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="IND02",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountyDesignator: Optional[X12ID] = element(
        name="IND03",
        description="County Designator",
        min_length=5,
        max_length=5,
    )

    CityName: Optional[X12AN] = element(
        name="IND04",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    LanguageCode: Optional[X12ID] = element(
        name="IND05",
        description="Language Code",
        min_length=2,
        max_length=3,
    )

    LanguageProficiencyIndicator: Optional[X12ID] = element(
        name="IND06",
        description="Language Proficiency Indicator",
    )

    LanguageCode2: Optional[X12ID] = element(
        name="IND07",
        description="Language Code",
        min_length=2,
        max_length=3,
    )

    LanguageCode3: Optional[X12ID] = element(
        name="IND08",
        description="Language Code",
        min_length=2,
        max_length=3,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="IND09",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="IND10",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="IND11",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="IND12",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
