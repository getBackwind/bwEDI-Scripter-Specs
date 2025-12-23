# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class USD(Segment):
    """
    USD - Usage-Sensitive Detail
    
    Description:
        To specify usage-sensitive details which qualify for discounts or are subject to special rates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/USD/
    """
    _id: Literal["USD"] = id_element(name="USD")

    RelationshipCode: X12ID = element(
        name="USD01",
        description="Relationship Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="USD02",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Rate: Optional[X12R] = element(
        name="USD03",
        description="Rate",
        min_length=1,
        max_length=9,
    )

    Percent: Optional[X12R] = element(
        name="USD04",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Quantity: Optional[X12R] = element(
        name="USD06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="USD07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="USD08",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Amount: Optional[X12Nn] = element(
        name="USD09",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    RangeMinimum: Optional[X12R] = element(
        name="USD11",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="USD12",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )
