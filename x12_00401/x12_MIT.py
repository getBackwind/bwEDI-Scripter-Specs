# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn


class MIT(Segment):
    """
    MIT - Message Identification
    
    Description:
        To identify the beginning of a specific message and to allow the identification of a subject for the message
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MIT/
    """
    _id: Literal["MIT"] = id_element(name="MIT")

    ReferenceIdentification: X12AN = element(
        name="MIT01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="MIT02",
        description="Description",
        min_length=1,
        max_length=80,
    )

    PageWidth: Optional[X12Nn] = element(
        name="MIT03",
        description="Page Width",
        min_length=1,
        max_length=3,
    )

    PageLengthLines: Optional[X12Nn] = element(
        name="MIT04",
        description="Page Length Lines",
        min_length=1,
        max_length=3,
    )
