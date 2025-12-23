# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class SCS(Segment):
    """
    SCS - Credit Score
    
    Description:
        To identify evaluation factors used in determining an applicant's credit score
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SCS/
    """
    _id: Literal["SCS"] = id_element(name="SCS")

    ReferenceIdentification: Optional[X12AN] = element(
        name="SCS01",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="SCS02",
        description="Free-Form Message Text",
        min_length=1,
        max_length=264,
    )
