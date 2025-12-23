# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class TSD(Segment):
    """
    TSD - Trailer Shipment Details
    
    Description:
        To specify details of shipments on a trailer
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TSD/
    """
    _id: Literal["TSD"] = id_element(name="TSD")

    AssignedIdentification: Optional[X12AN] = element(
        name="TSD01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    Position: Optional[X12AN] = element(
        name="TSD02",
        description="Position",
        min_length=1,
        max_length=3,
    )
