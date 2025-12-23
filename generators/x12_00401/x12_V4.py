# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class V4(Segment):
    """
    V4 - Cargo Location Reference
    
    Description:
        To specify the cargo location on board the vessel
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/V4/
    """
    _id: Literal["V4"] = id_element(name="V4")

    VesselStowageLocation: X12AN = element(
        name="V401",
        description="Vessel Stowage Location",
        mandatory=True,
        min_length=1,
        max_length=12,
    )
