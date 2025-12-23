# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class LN2(Segment):
    """
    LN2 - Existing Real Estate Loan Specific Data
    
    Description:
        To provide specific information about a real estate loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LN2/
    """
    _id: Literal["LN2"] = id_element(name="LN2")

    LienPriorityCode: X12ID = element(
        name="LN201",
        description="Lien Priority Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    RealEstateLoanTypeCode: X12ID = element(
        name="LN202",
        description="Real Estate Loan Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Percent: Optional[X12R] = element(
        name="LN203",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    FrequencyCode: Optional[X12ID] = element(
        name="LN204",
        description="Frequency Code",
        min_length=1,
        max_length=1,
    )

    LoanPaymentTypeCode: Optional[X12ID] = element(
        name="LN205",
        description="Loan Payment Type Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="LN206",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    AssumptionTermsCode: Optional[X12ID] = element(
        name="LN207",
        description="Assumption Terms Code",
        min_length=1,
        max_length=1,
    )

    Name: Optional[X12AN] = element(
        name="LN208",
        description="Name",
        min_length=1,
        max_length=60,
    )

    QuantityQualifier: Optional[X12ID] = element(
        name="LN210",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="LN211",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="LN212",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
