# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn


class T8(Segment):
    """
    T8 - Free-form Transit Data
    
    Description:
        To transmit information in a free-form format relating to a specified transit sequence number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/T8/
    """
    _id: Literal["T8"] = id_element(name="T8")

    AssignedNumber: X12Nn = element(
        name="T801",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    FreeFormTransitData: X12AN = element(
        name="T802",
        description="Free-form Transit Data",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
