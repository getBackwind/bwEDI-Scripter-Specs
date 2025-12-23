# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class F10(Segment):
    """
    F10 - Identification of Claim (Tracer)
    
    Description:
        To identify a loss or damage claim
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/F10/
    """
    _id: Literal["F10"] = id_element(name="F10")

    Date: X12DT = element(
        name="F1001",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: X12AN = element(
        name="F1002",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="F1003",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="F1004",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )
