# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class INC(Segment):
    """
    INC - Installment Information
    
    Description:
        To specify installment billing arrangement
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/INC/
    """
    _id: Literal["INC"] = id_element(name="INC")

    TermsTypeCode: X12ID = element(
        name="INC01",
        description="Terms Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="INC03",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="INC04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="INC05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="INC06",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )
