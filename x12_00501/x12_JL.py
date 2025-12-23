# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class JL(Segment):
    """
    JL - Journal Identification
    
    Description:
        To indicate the carrier, date, time, and individual making a journal entry
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/JL/
    """
    _id: Literal["JL"] = id_element(name="JL")

    StandardCarrierAlphaCode: X12ID = element(
        name="JL01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Date: X12DT = element(
        name="JL02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: X12TM = element(
        name="JL03",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    Name: Optional[X12AN] = element(
        name="JL04",
        description="Name",
        min_length=1,
        max_length=60,
    )
