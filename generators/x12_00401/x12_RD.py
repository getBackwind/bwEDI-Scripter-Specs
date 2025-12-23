# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class RD(Segment):
    """
    RD - Rate Data
    
    Description:
        To indicate the through rate
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RD/
    """
    _id: Literal["RD"] = id_element(name="RD")

    AssignedNumber: X12Nn = element(
        name="RD01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    RateApplicationTypeCode: X12ID = element(
        name="RD02",
        description="Rate Application Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    FreightRate: X12R = element(
        name="RD03",
        description="Freight Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    ChangeTypeCode: X12ID = element(
        name="RD04",
        description="Change Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
