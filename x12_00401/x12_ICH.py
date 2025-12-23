# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class ICH(Segment):
    """
    ICH - Individual Characteristics
    
    Description:
        To provide personal information on an individual
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ICH/
    """
    _id: Literal["ICH"] = id_element(name="ICH")

    Count: Optional[X12Nn] = element(
        name="ICH01",
        description="Count",
        min_length=1,
        max_length=9,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="ICH02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="ICH03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    GenderCode: Optional[X12ID] = element(
        name="ICH04",
        description="Gender Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ICH05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="ICH06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="ICH07",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    OccupationCode: Optional[X12ID] = element(
        name="ICH08",
        description="Occupation Code",
        min_length=4,
        max_length=6,
    )

    IndividualRelationshipCode: Optional[X12ID] = element(
        name="ICH09",
        description="Individual Relationship Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="ICH10",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Description2: Optional[X12AN] = element(
        name="ICH11",
        description="Description",
        min_length=1,
        max_length=80,
    )

    PoliticalPartyAffiliationCode: Optional[X12ID] = element(
        name="ICH12",
        description="Political Party Affiliation Code",
        min_length=2,
        max_length=2,
    )
