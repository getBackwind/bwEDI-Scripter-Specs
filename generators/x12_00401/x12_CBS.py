# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12R


class CBS(Segment):
    """
    CBS - Cost Breakdown Structure
    
    Description:
        To identify and quantify each line item being proposed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CBS/
    """
    _id: Literal["CBS"] = id_element(name="CBS")

    AssignedIdentification: X12AN = element(
        name="CBS01",
        description="Assigned Identification",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    Quantity: X12R = element(
        name="CBS02",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )
