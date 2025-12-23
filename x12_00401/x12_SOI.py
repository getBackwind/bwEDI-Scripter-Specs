# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class SOI(Segment):
    """
    SOI - Source of Income
    
    Description:
        To define the source and related information about the income being reported
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SOI/
    """
    _id: Literal["SOI"] = id_element(name="SOI")

    TypeOfIncomeCode: X12ID = element(
        name="SOI01",
        description="Type of Income Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="SOI02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="SOI03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    Number: Optional[X12Nn] = element(
        name="SOI04",
        description="Number",
        min_length=1,
        max_length=9,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SOI05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
