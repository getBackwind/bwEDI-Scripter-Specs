# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class RDD(Segment):
    """
    RDD - Route Description Detail
    
    Description:
        To identify routing detail for carriers participating in a route
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RDD/
    """
    _id: Literal["RDD"] = id_element(name="RDD")

    StandardCarrierAlphaCode: X12ID = element(
        name="RDD01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Rule260JunctionCode: Optional[X12ID] = element(
        name="RDD02",
        description="Rule 260 Junction Code",
        min_length=1,
        max_length=5,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="RDD03",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Rule260JunctionCode2: Optional[X12ID] = element(
        name="RDD04",
        description="Rule 260 Junction Code",
        min_length=1,
        max_length=5,
    )

    AssignedNumber: Optional[X12Nn] = element(
        name="RDD05",
        description="Assigned Number",
        min_length=1,
        max_length=6,
    )
