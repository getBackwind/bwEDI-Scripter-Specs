# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class ARC(Segment):
    """
    ARC - Animal Results Counts
    
    Description:
        To record the number of results reported for each test or observation type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ARC/
    """
    _id: Literal["ARC"] = id_element(name="ARC")

    Count: X12Nn = element(
        name="ARC01",
        description="Count",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    TestTypeCode: Optional[X12ID] = element(
        name="ARC02",
        description="Test Type Code",
        min_length=2,
        max_length=2,
    )

    ObservationTypeCode: Optional[X12ID] = element(
        name="ARC03",
        description="Observation Type Code",
        min_length=2,
        max_length=2,
    )
