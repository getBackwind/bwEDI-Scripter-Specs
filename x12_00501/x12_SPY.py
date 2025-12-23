# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SPY(Segment):
    """
    SPY - Scope of Power of Attorney
    
    Description:
        To identify the scope of a power of attorney
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SPY/
    """
    _id: Literal["SPY"] = id_element(name="SPY")

    ActionCode: X12ID = element(
        name="SPY01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ScopeOfPowerOfAttorneyIdentificationCode: Optional[X12ID] = element(
        name="SPY02",
        description="Scope of Power of Attorney Identification Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="SPY03",
        description="Description",
        min_length=1,
        max_length=80,
    )
