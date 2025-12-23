# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class PRD(Segment):
    """
    PRD - Mortgage Loan Product Description
    
    Description:
        To describe terms of a mortgage product
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PRD/
    """
    _id: Literal["PRD"] = id_element(name="PRD")

    LoanPaymentTypeCode: X12ID = element(
        name="PRD01",
        description="Loan Payment Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="PRD02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="PRD03",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    LoanRateTypeCode: Optional[X12ID] = element(
        name="PRD04",
        description="Loan Rate Type Code",
        min_length=1,
        max_length=1,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="PRD05",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    Quantity2: Optional[X12R] = element(
        name="PRD06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="PRD07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PRD08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="PRD09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity4: Optional[X12R] = element(
        name="PRD10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PRD11",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
