# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class RCR(Segment):
    """
    RCR - Reporting Criteria
    
    Description:
        To specify the criteria for reporting product activity and timing
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RCR/
    """
    _id: Literal["RCR"] = id_element(name="RCR")

    TimingQualifier: X12ID = element(
        name="RCR01",
        description="Timing Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ActivityCode: X12ID = element(
        name="RCR02",
        description="Activity Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )
