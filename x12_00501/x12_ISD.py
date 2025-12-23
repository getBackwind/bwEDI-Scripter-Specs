# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12TM


class ISD(Segment):
    """
    ISD - Railroad Interline Service Definition Detail
    
    Description:
        To identify service commitment starting events
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ISD/
    """
    _id: Literal["ISD"] = id_element(name="ISD")

    StandardCarrierAlphaCode: X12ID = element(
        name="ISD01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardPointLocationCode: X12ID = element(
        name="ISD02",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    EventCode: X12ID = element(
        name="ISD03",
        description="Event Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Time: X12TM = element(
        name="ISD04",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )
