# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class PEX(Segment):
    """
    PEX - Property or Housing Expense
    
    Description:
        To provide housing expense information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PEX/
    """
    _id: Literal["PEX"] = id_element(name="PEX")

    GeneralExpenseQualifier: X12ID = element(
        name="PEX01",
        description="General Expense Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="PEX02",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="PEX03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    TaxTypeCode: Optional[X12ID] = element(
        name="PEX04",
        description="Tax Type Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="PEX05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="PEX06",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    TaxExemptCode: Optional[X12ID] = element(
        name="PEX07",
        description="Tax Exempt Code",
        min_length=1,
        max_length=1,
    )
