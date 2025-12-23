# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class AT1(Segment):
    """
    AT1 - Bill of Lading Line Item Number
    
    Description:
        To reference a Bill of Lading line number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AT1/
    """
    _id: Literal["AT1"] = id_element(name="AT1")

    LadingLineItemNumber: X12Nn = element(
        name="AT101",
        description="Lading Line Item Number",
        mandatory=True,
        min_length=1,
        max_length=3,
    )
