# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class NTE(Segment):
    """
    NTE - Note/Special Instruction
    
    Description:
        To transmit information in a free-form format, if necessary, for comment or special instruction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/NTE/
    """
    _id: Literal["NTE"] = id_element(name="NTE")

    ReferenceCode: Optional[X12ID] = element(
        name="NTE01",
        description="Note Reference Code",
        min_length=3,
        max_length=3,
    )

    Description: X12AN = element(
        name="NTE02",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
