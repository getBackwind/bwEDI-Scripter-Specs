# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class CA1(Segment):
    """
    CA1 - Rate Request Identifier
    
    Description:
        To identify the rate request identification number and any applicable suffix
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CA1/
    """
    _id: Literal["CA1"] = id_element(name="CA1")

    RateRequestID: X12Nn = element(
        name="CA101",
        description="Rate Request ID",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    RateResponseSuffix: Optional[X12Nn] = element(
        name="CA102",
        description="Rate Response Suffix",
        min_length=1,
        max_length=3,
    )
