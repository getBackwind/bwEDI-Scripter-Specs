# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class RB(Segment):
    """
    RB - Rate/Minimum Detail
    
    Description:
        To indicate the minimum units required and the through rate
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RB/
    """
    _id: Literal["RB"] = id_element(name="RB")

    AssignedNumber: X12Nn = element(
        name="RB01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    RateApplicationTypeCode: X12ID = element(
        name="RB02",
        description="Rate Application Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    FreightRate: X12R = element(
        name="RB03",
        description="Freight Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    MinimumWeightLogic: Optional[X12AN] = element(
        name="RB04",
        description="Minimum/Weight Logic",
        min_length=1,
        max_length=2,
    )

    LoadingRestriction: Optional[X12Nn] = element(
        name="RB05",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    LoadingRestriction2: Optional[X12Nn] = element(
        name="RB06",
        description="Loading Restriction",
        min_length=1,
        max_length=7,
    )

    Percent: Optional[X12Nn] = element(
        name="RB07",
        description="Percent",
        min_length=1,
        max_length=3,
    )

    ChangeTypeCode: X12ID = element(
        name="RB08",
        description="Change Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
