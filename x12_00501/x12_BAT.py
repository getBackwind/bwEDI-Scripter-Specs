# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BAT(Segment):
    """
    BAT - Batch
    
    Description:
        To indicate batch identifying information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BAT/
    """
    _id: Literal["BAT"] = id_element(name="BAT")

    Date: Optional[X12DT] = element(
        name="BAT01",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BAT02",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BAT03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    BatchTypeCode: Optional[X12ID] = element(
        name="BAT04",
        description="Batch Type Code",
        min_length=2,
        max_length=2,
    )
