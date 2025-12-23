# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class WGP(Segment):
    """
    WGP - Tariff Weight Group
    
    Description:
        To identify low-value break of the specific weight groups used when applying rates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/WGP/
    """
    _id: Literal["WGP"] = id_element(name="WGP")

    Weight: Optional[X12R] = element(
        name="WGP01",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight2: Optional[X12R] = element(
        name="WGP02",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight3: Optional[X12R] = element(
        name="WGP03",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight4: Optional[X12R] = element(
        name="WGP04",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight5: Optional[X12R] = element(
        name="WGP05",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight6: Optional[X12R] = element(
        name="WGP06",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight7: Optional[X12R] = element(
        name="WGP07",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight8: Optional[X12R] = element(
        name="WGP08",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight9: Optional[X12R] = element(
        name="WGP09",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight10: Optional[X12R] = element(
        name="WGP10",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight11: Optional[X12R] = element(
        name="WGP11",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight12: Optional[X12R] = element(
        name="WGP12",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight13: Optional[X12R] = element(
        name="WGP13",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight14: Optional[X12R] = element(
        name="WGP14",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight15: Optional[X12R] = element(
        name="WGP15",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Weight16: Optional[X12R] = element(
        name="WGP16",
        description="Weight",
        min_length=1,
        max_length=10,
    )
