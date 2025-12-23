# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT


class V3(Segment):
    """
    V3 - Vessel Schedule
    
    Description:
        To transmit vessel scheduling information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/V3/
    """
    _id: Literal["V3"] = id_element(name="V3")

    CurrentPortOfLoading: X12AN = element(
        name="V301",
        description="Current Port of Loading",
        mandatory=True,
        min_length=2,
        max_length=24,
    )

    Date: X12DT = element(
        name="V302",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    NextPortOfDischarge: Optional[X12AN] = element(
        name="V303",
        description="Next Port of Discharge",
        min_length=2,
        max_length=24,
    )

    Date2: Optional[X12DT] = element(
        name="V304",
        description="Date",
        min_length=8,
        max_length=8,
    )
