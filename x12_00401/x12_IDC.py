# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class IDC(Segment):
    """
    IDC - Identification Card
    
    Description:
        To provide notification to produce replacement identification card(s)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IDC/
    """
    _id: Literal["IDC"] = id_element(name="IDC")

    PlanCoverageDescription: X12AN = element(
        name="IDC01",
        description="Plan Coverage Description",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    IdentificationCardTypeCode: X12ID = element(
        name="IDC02",
        description="Identification Card Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="IDC03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ActionCode: Optional[X12ID] = element(
        name="IDC04",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
