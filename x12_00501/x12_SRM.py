# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class SRM(Segment):
    """
    SRM - Scale Rates
    
    Description:
        To indicate rates as defined in scale rate route
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SRM/
    """
    _id: Literal["SRM"] = id_element(name="SRM")

    FreightRate: Optional[X12R] = element(
        name="SRM01",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate2: Optional[X12R] = element(
        name="SRM02",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate3: Optional[X12R] = element(
        name="SRM03",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate4: Optional[X12R] = element(
        name="SRM04",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate5: Optional[X12R] = element(
        name="SRM05",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate6: Optional[X12R] = element(
        name="SRM06",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate7: Optional[X12R] = element(
        name="SRM07",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate8: Optional[X12R] = element(
        name="SRM08",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate9: Optional[X12R] = element(
        name="SRM09",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate10: Optional[X12R] = element(
        name="SRM10",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate11: Optional[X12R] = element(
        name="SRM11",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate12: Optional[X12R] = element(
        name="SRM12",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate13: Optional[X12R] = element(
        name="SRM13",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate14: Optional[X12R] = element(
        name="SRM14",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate15: Optional[X12R] = element(
        name="SRM15",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    FreightRate16: Optional[X12R] = element(
        name="SRM16",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )
