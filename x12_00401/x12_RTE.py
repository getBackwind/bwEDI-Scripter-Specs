# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class RTE(Segment):
    """
    RTE - Rate Information
    
    Description:
        To specify the earnings, rates and multipliers for this account
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RTE/
    """
    _id: Literal["RTE"] = id_element(name="RTE")

    RateQualifier: X12ID = element(
        name="RTE01",
        description="Rate Qualifier",
        mandatory=True,
    )

    InterestRate: X12R = element(
        name="RTE02",
        description="Interest Rate",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="RTE03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Number: Optional[X12Nn] = element(
        name="RTE04",
        description="Number",
        min_length=1,
        max_length=9,
    )

    Number2: Optional[X12Nn] = element(
        name="RTE05",
        description="Number",
        min_length=1,
        max_length=9,
    )
