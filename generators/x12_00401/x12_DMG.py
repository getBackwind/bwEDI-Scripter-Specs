# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DMG(Segment):
    """
    DMG - Demographic Information
    
    Description:
        To supply demographic information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DMG/
    """
    _id: Literal["DMG"] = id_element(name="DMG")

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="DMG01",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="DMG02",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    GenderCode: Optional[X12ID] = element(
        name="DMG03",
        description="Gender Code",
        min_length=1,
        max_length=1,
    )

    MaritalStatusCode: Optional[X12ID] = element(
        name="DMG04",
        description="Marital Status Code",
        min_length=1,
        max_length=1,
    )

    RaceOrEthnicityCode: Optional[X12ID] = element(
        name="DMG05",
        description="Race or Ethnicity Code",
        min_length=1,
        max_length=1,
    )

    CitizenshipStatusCode: Optional[X12ID] = element(
        name="DMG06",
        description="Citizenship Status Code",
        min_length=1,
        max_length=1,
    )

    CountryCode: Optional[X12ID] = element(
        name="DMG07",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    BasisOfVerificationCode: Optional[X12ID] = element(
        name="DMG08",
        description="Basis of Verification Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="DMG09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
