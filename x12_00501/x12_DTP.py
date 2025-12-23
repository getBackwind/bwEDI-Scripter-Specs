# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class DTP(Segment):
    """
    DTP - Date or Time or Period
    
    Description:
        To specify any or all of a date, a time, or a time period
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DTP/
    """
    _id: Literal["DTP"] = id_element(name="DTP")

    DateTimeQualifier: X12ID = element(
        name="DTP01",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: X12ID = element(
        name="DTP02",
        description="Date Time Period Format Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: X12AN = element(
        name="DTP03",
        description="Date Time Period",
        mandatory=True,
        min_length=1,
        max_length=35,
    )
