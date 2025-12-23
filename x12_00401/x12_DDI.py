# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class DDI(Segment):
    """
    DDI - Description
    
    Description:
        To provide description information related to the electronic form of the X12 standards
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DDI/
    """
    _id: Literal["DDI"] = id_element(name="DDI")

    Description: X12AN = element(
        name="DDI01",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
