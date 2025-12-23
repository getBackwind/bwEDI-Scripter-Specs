# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class RAT(Segment):
    """
    RAT - Adjustable Rate Description
    
    Description:
        To describe terms of rate adjustment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RAT/
    """
    _id: Literal["RAT"] = id_element(name="RAT")

    Quantity: X12R = element(
        name="RAT02",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    IndexIdentityCode: X12ID = element(
        name="RAT03",
        description="Index Identity Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Percent: X12R = element(
        name="RAT04",
        description="Percent",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    Percent2: X12R = element(
        name="RAT05",
        description="Percent",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    Percent3: X12R = element(
        name="RAT06",
        description="Percent",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    Quantity2: X12R = element(
        name="RAT08",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="RAT10",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="RAT11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Percent4: Optional[X12R] = element(
        name="RAT12",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Percent5: Optional[X12R] = element(
        name="RAT13",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    Percent6: Optional[X12R] = element(
        name="RAT14",
        description="Percent",
        min_length=1,
        max_length=10,
    )

    RoundingSystemCode: Optional[X12ID] = element(
        name="RAT15",
        description="Rounding System Code",
        min_length=1,
        max_length=1,
    )

    RateLifeCapSourceCode: Optional[X12ID] = element(
        name="RAT16",
        description="Rate Life Cap Source Code",
    )

    Percent7: Optional[X12R] = element(
        name="RAT17",
        description="Percent",
        min_length=1,
        max_length=10,
    )
