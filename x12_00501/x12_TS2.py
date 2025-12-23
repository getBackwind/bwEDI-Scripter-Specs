# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class TS2(Segment):
    """
    TS2 - Transaction Supplemental Statistics
    
    Description:
        To provide supplemental summary control information by provider fiscal year and bill type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TS2/
    """
    _id: Literal["TS2"] = id_element(name="TS2")

    MonetaryAmount: Optional[X12R] = element(
        name="TS201",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="TS202",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="TS203",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="TS204",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="TS205",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="TS206",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="TS207",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount7: Optional[X12R] = element(
        name="TS208",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount8: Optional[X12R] = element(
        name="TS209",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity2: Optional[X12R] = element(
        name="TS210",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="TS211",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity4: Optional[X12R] = element(
        name="TS212",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity5: Optional[X12R] = element(
        name="TS213",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity6: Optional[X12R] = element(
        name="TS214",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount9: Optional[X12R] = element(
        name="TS215",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity7: Optional[X12R] = element(
        name="TS216",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    MonetaryAmount10: Optional[X12R] = element(
        name="TS217",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount11: Optional[X12R] = element(
        name="TS218",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount12: Optional[X12R] = element(
        name="TS219",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
