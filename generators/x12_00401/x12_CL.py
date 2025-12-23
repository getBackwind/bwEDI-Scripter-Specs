# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class CL(Segment):
    """
    CL - Class
    
    Description:
        To identify tariff class
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CL/
    """
    _id: Literal["CL"] = id_element(name="CL")

    FreightClassCode: X12AN = element(
        name="CL01",
        description="Freight Class Code",
        mandatory=True,
        min_length=2,
        max_length=5,
    )
