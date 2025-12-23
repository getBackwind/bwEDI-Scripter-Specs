# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class IDB(Segment):
    """
    IDB - Indebtedness for Student Loans
    
    Description:
        To provide information about previously guaranteed student loans
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IDB/
    """
    _id: Literal["IDB"] = id_element(name="IDB")

    LoanTypeCode: X12ID = element(
        name="IDB01",
        description="Loan Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    AmountQualifierCode: X12ID = element(
        name="IDB02",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: X12R = element(
        name="IDB03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    InterestRate: Optional[X12R] = element(
        name="IDB04",
        description="Interest Rate",
        min_length=1,
        max_length=6,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="IDB05",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )
