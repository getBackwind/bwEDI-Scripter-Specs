# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12TM


class G62(Segment):
    """
    G62 - Date/Time
    
    Description:
        To specify pertinent dates and times
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G62/
    """
    _id: Literal["G62"] = id_element(name="G62")

    DateQualifier: Optional[X12ID] = element(
        name="G6201",
        description="Date Qualifier",
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="G6202",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TimeQualifier: Optional[X12ID] = element(
        name="G6203",
        description="Time Qualifier",
        min_length=1,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="G6204",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="G6205",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
