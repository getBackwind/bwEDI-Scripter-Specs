# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class RAB(Segment):
    """
    RAB - Rate or Minimum Qualifiers
    
    Description:
        To indicate codes qualifying rates and the minimums
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RAB/
    """
    _id: Literal["RAB"] = id_element(name="RAB")

    RateValueQualifier: Optional[X12ID] = element(
        name="RAB01",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="RAB02",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )

    AlternationPrecedenceCode: Optional[X12ID] = element(
        name="RAB03",
        description="Alternation Precedence Code",
        min_length=1,
        max_length=1,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="RAB04",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MinimumWeightLogic: Optional[X12AN] = element(
        name="RAB05",
        description="Minimum/Weight Logic",
        min_length=1,
        max_length=2,
    )

    LoadingRestriction: Optional[X12Nn] = element(
        name="RAB06",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction2: Optional[X12Nn] = element(
        name="RAB07",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    PercentIntegerFormat: Optional[X12Nn] = element(
        name="RAB08",
        description="Percent, Integer Format",
        min_length=1,
        max_length=3,
    )

    UnitConversionFactor: Optional[X12Nn] = element(
        name="RAB09",
        description="Unit Conversion Factor",
        min_length=1,
        max_length=9,
    )

    AssignedNumber2: Optional[X12Nn] = element(
        name="RAB10",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )
