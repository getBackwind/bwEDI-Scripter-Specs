# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class RTS(Segment):
    """
    RTS - Tariff Rates
    
    Description:
        To transmit tariff freight rates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RTS/
    """
    _id: Literal["RTS"] = id_element(name="RTS")

    FreightRate: Optional[X12R] = element(
        name="RTS01",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate2: Optional[X12R] = element(
        name="RTS02",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate3: Optional[X12R] = element(
        name="RTS03",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate4: Optional[X12R] = element(
        name="RTS04",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate5: Optional[X12R] = element(
        name="RTS05",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate6: Optional[X12R] = element(
        name="RTS06",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate7: Optional[X12R] = element(
        name="RTS07",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate8: Optional[X12R] = element(
        name="RTS08",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate9: Optional[X12R] = element(
        name="RTS09",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate10: Optional[X12R] = element(
        name="RTS10",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate11: Optional[X12R] = element(
        name="RTS11",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate12: Optional[X12R] = element(
        name="RTS12",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate13: Optional[X12R] = element(
        name="RTS13",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate14: Optional[X12R] = element(
        name="RTS14",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate15: Optional[X12R] = element(
        name="RTS15",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate16: Optional[X12R] = element(
        name="RTS16",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )
