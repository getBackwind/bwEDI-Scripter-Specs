# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MTX(Segment):
    """
    MTX - Text
    
    Description:
        To specify textual data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MTX/
    """
    _id: Literal["MTX"] = id_element(name="MTX")

    NoteReferenceCode: Optional[X12ID] = element(
        name="MTX01",
        description="Note Reference Code",
        min_length=3,
        max_length=3,
    )

    Text: Optional[X12AN] = element(
        name="MTX02",
        description="Message Text",
        min_length=1,
        max_length=4096,
    )

    Text2: Optional[X12AN] = element(
        name="MTX03",
        description="Message Text",
        min_length=1,
        max_length=4096,
    )

    PrinterControlCode: Optional[X12ID] = element(
        name="MTX04",
        description="Printer Carriage Control Code",
        min_length=2,
        max_length=2,
    )
