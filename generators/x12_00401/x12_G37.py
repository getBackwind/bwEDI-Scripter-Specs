# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12TM


class G37(Segment):
    """
    G37 - Labor Activity
    
    Description:
        To indicate the type of activity performed and the start and end times for the activity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G37/
    """
    _id: Literal["G37"] = id_element(name="G37")

    LaborActivityCode: X12ID = element(
        name="G3701",
        description="Labor Activity Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Time: Optional[X12TM] = element(
        name="G3702",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="G3703",
        description="Time",
        min_length=4,
        max_length=8,
    )
