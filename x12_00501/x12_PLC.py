# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn


class PLC(Segment):
    """
    PLC - Equipment Placement Information
    
    Description:
        To specify the placement number and identification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PLC/
    """
    _id: Literal["PLC"] = id_element(name="PLC")

    Number: X12Nn = element(
        name="PLC01",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PLC02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
