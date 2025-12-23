# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class NCA(Segment):
    """
    NCA - Nonconformance Action
    
    Description:
        To specify the action that is to be taken in response to a nonconformance condition
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/NCA/
    """
    _id: Literal["NCA"] = id_element(name="NCA")

    AssignedIdentification: Optional[X12AN] = element(
        name="NCA01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    NonconformanceResultantResponseCode: Optional[X12ID] = element(
        name="NCA02",
        description="Nonconformance Resultant Response Code",
        min_length=1,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="NCA03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    Quantity: Optional[X12R] = element(
        name="NCA04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
