# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DOS(Segment):
    """
    DOS - Definition of Share
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DOS/
    """
    _id: Literal["DOS"] = id_element(name="DOS")

    ContractTypeCode: X12ID = element(
        name="DOS01",
        description="Contract Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="DOS02",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="DOS03",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="DOS04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    PercentageAsDecimal2: Optional[X12R] = element(
        name="DOS05",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    EntityIdentifierCode: Optional[X12ID] = element(
        name="DOS06",
        description="Entity Identifier Code",
        min_length=2,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="DOS07",
        description="Description",
        min_length=1,
        max_length=80,
    )
