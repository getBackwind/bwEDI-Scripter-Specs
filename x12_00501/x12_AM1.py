# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class AM1(Segment):
    """
    AM1 - Informational Values
    
    Description:
        To specify a code and the amount or quantity or percentage associated with it
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AM1/
    """
    _id: Literal["AM1"] = id_element(name="AM1")

    CodeCategory: X12ID = element(
        name="AM101",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceIDQualifier: X12ID = element(
        name="AM102",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="AM103",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="AM104",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="AM105",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="AM106",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
