# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class DN(Segment):
    """
    DN - Dealer Effectivity
    
    Description:
        To indicate a change in dealer status
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DN/
    """
    _id: Literal["DN"] = id_element(name="DN")

    DateQualifier: X12ID = element(
        name="DN01",
        description="Date Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="DN02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    DemandArea: Optional[X12AN] = element(
        name="DN03",
        description="Demand Area",
        min_length=3,
        max_length=3,
    )

    FinancialStatus: Optional[X12AN] = element(
        name="DN04",
        description="Financial Status",
        min_length=3,
        max_length=3,
    )
