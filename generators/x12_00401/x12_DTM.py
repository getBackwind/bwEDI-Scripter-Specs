# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class DTM(Segment):
    """
    DTM - Date/Time Reference
    
    Description:
        To specify pertinent dates and times
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DTM/
    """
    _id: Literal["DTM"] = id_element(name="DTM")

    DateTimeQualifier: X12ID = element(
        name="DTM01",
        description="Date/Time Qualifier",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="DTM02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="DTM03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="DTM04",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="DTM05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="DTM06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
