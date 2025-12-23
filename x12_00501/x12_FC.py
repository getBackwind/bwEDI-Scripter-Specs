# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class FC(Segment):
    """
    FC - Financial Contribution
    
    Description:
        To specify the financial contribution information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FC/
    """
    _id: Literal["FC"] = id_element(name="FC")

    ContributionCode: X12ID = element(
        name="FC01",
        description="Contribution Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="FC02",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="FC03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Number: Optional[X12Nn] = element(
        name="FC04",
        description="Number",
        min_length=1,
        max_length=9,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="FC05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
