# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class SB(Segment):
    """
    SB - Docket Level
    
    Description:
        To indicate the docket level
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SB/
    """
    _id: Literal["SB"] = id_element(name="SB")

    DocketLevelNumber: X12Nn = element(
        name="SB01",
        description="Docket Level Number",
        mandatory=True,
        min_length=1,
        max_length=2,
    )
