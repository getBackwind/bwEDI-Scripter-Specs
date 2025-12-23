# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class RPA(Segment):
    """
    RPA - Rate Amounts or Percents
    
    Description:
        To identify rate amounts or percents for a specific cost or other line item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RPA/
    """
    _id: Literal["RPA"] = id_element(name="RPA")

    RateOrValueTypeCode: X12ID = element(
        name="RPA01",
        description="Rate or Value Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="RPA02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Rate: Optional[X12R] = element(
        name="RPA03",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="RPA05",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
