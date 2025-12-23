# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class RTT(Segment):
    """
    RTT - Freight Rate Information
    
    Description:
        To transmit a rate
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RTT/
    """
    _id: Literal["RTT"] = id_element(name="RTT")

    RateValueQualifier: X12ID = element(
        name="RTT01",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FreightRate: X12R = element(
        name="RTT02",
        description="Freight Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )
