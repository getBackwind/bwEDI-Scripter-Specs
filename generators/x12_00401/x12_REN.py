# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class REN(Segment):
    """
    REN - Rate Request Information
    
    Description:
        To specify primary identification data for request or information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/REN/
    """
    _id: Literal["REN"] = id_element(name="REN")

    RateRequestResponseCode: X12ID = element(
        name="REN01",
        description="Rate Request/Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="REN02",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Description: Optional[X12AN] = element(
        name="REN03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="REN04",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    RateRequestResponseCode2: Optional[X12ID] = element(
        name="REN05",
        description="Rate Request/Response Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="REN06",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="REN07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
