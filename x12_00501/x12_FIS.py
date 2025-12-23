# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class FIS(Segment):
    """
    FIS - Mortgage Loan Fiscal Data
    
    Description:
        To specify mortgage loan fiscal data when applying for insurance claim benefits
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FIS/
    """
    _id: Literal["FIS"] = id_element(name="FIS")

    AmountQualifierCode: X12ID = element(
        name="FIS01",
        description="Amount Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="FIS02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="FIS03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="FIS04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
