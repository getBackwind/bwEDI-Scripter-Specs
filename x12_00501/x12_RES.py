# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class RES(Segment):
    """
    RES - Real Estate Sales Price Change
    
    Description:
        To provide the type, source, and amount of real estate sales price changes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RES/
    """
    _id: Literal["RES"] = id_element(name="RES")

    RealEstateSalesPriceChangeCode: X12ID = element(
        name="RES01",
        description="Real Estate Sales Price Change Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    SourceOfFundsCode: Optional[X12ID] = element(
        name="RES02",
        description="Source of Funds Code",
        min_length=1,
        max_length=1,
    )

    TypeOfFundsCode: Optional[X12ID] = element(
        name="RES03",
        description="Type of Funds Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="RES04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Description: Optional[X12AN] = element(
        name="RES05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="RES06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Date: Optional[X12DT] = element(
        name="RES07",
        description="Date",
        min_length=8,
        max_length=8,
    )
