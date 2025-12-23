# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class RS(Segment):
    """
    RS - Rate Subset
    
    Description:
        To indicate effective or expiration dates for rates and divisions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RS/
    """
    _id: Literal["RS"] = id_element(name="RS")

    AssignedNumber: X12Nn = element(
        name="RS01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    Number: X12Nn = element(
        name="RS02",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    RateLevelQualifierCode: Optional[X12ID] = element(
        name="RS03",
        description="Rate Level Qualifier Code",
        min_length=1,
        max_length=1,
    )

    RateLevel: Optional[X12AN] = element(
        name="RS04",
        description="Rate Level",
        min_length=1,
        max_length=5,
    )

    Date: Optional[X12DT] = element(
        name="RS05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="RS06",
        description="Date",
        min_length=8,
        max_length=8,
    )
