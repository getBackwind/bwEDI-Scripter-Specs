# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class G91(Segment):
    """
    G91 - Price Change Status
    
    Description:
        To enable the supplier/broker to change pricing information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G91/
    """
    _id: Literal["G91"] = id_element(name="G91")

    ChangeTypeCode: X12ID = element(
        name="G9101",
        description="Change Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
