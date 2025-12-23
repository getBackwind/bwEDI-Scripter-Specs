# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class N12(Segment):
    """
    N12 - Equipment Environment
    
    Description:
        To describe the operating environment of the equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N12/
    """
    _id: Literal["N12"] = id_element(name="N12")

    FuelType: X12ID = element(
        name="N1201",
        description="Fuel Type",
        mandatory=True,
    )
