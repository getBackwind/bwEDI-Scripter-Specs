# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class G30(Segment):
    """
    G30 - Retail Account Marketing Types
    
    Description:
        To identify the type and number of marketing equipment or programs in a retail account
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G30/
    """
    _id: Literal["G30"] = id_element(name="G30")

    MarketingTypeCode: X12ID = element(
        name="G3001",
        description="Marketing Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Number: Optional[X12Nn] = element(
        name="G3002",
        description="Number",
        min_length=1,
        max_length=9,
    )
