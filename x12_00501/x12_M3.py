# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12TM


class M3(Segment):
    """
    M3 - Release
    
    Description:
        To indicate that the equipment is or is not to be released
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/M3/
    """
    _id: Literal["M3"] = id_element(name="M3")

    ReleaseCode: X12ID = element(
        name="M301",
        description="Release Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="M302",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="M303",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="M304",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
