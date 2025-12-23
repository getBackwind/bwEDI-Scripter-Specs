# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class MSG(Segment):
    """
    MSG - Message Text
    
    Description:
        To provide a free-form format that allows the transmission of text information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MSG/
    """
    _id: Literal["MSG"] = id_element(name="MSG")

    Message: X12AN = element(
        name="MSG01",
        description="Free-form Message Text",
        mandatory=True,
        min_length=1,
        max_length=264,
    )

    PrinterCarriageControlCode: Optional[X12ID] = element(
        name="MSG02",
        description="Printer Carriage Control Code",
        min_length=2,
        max_length=2,
    )

    Number: Optional[X12Nn] = element(
        name="MSG03",
        description="Number",
        min_length=1,
        max_length=9,
    )
