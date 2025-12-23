# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class BFS(Segment):
    """
    BFS - Borrower Financial Summary
    
    Description:
        To provide summary totals for borrower's financial position
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BFS/
    """
    _id: Literal["BFS"] = id_element(name="BFS")

    RateValueQualifier: Optional[X12ID] = element(
        name="BFS01",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="BFS02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    RateValueQualifier2: Optional[X12ID] = element(
        name="BFS03",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="BFS04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Date: Optional[X12DT] = element(
        name="BFS05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="BFS06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Date2: Optional[X12DT] = element(
        name="BFS07",
        description="Date",
        min_length=8,
        max_length=8,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="BFS08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    TypeOfIncomeCode: Optional[X12ID] = element(
        name="BFS09",
        description="Type of Income Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="BFS10",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
