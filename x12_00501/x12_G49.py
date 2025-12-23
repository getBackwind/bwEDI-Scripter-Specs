# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class G49(Segment):
    """
    G49 - Statement Total
    
    Description:
        To provide essential billing totals to the purchaser
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G49/
    """
    _id: Literal["G49"] = id_element(name="G49")

    Amount: X12Nn = element(
        name="G4901",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Amount2: Optional[X12Nn] = element(
        name="G4902",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount3: Optional[X12Nn] = element(
        name="G4903",
        description="Amount",
        min_length=1,
        max_length=15,
    )
