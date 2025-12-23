# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class L11(Segment):
    """
    L11 - Business Instructions and Reference Number
    
    Description:
        To specify instructions in this business relationship or a reference number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/L11/
    """
    _id: Literal["L11"] = id_element(name="L11")

    ReferenceIdentification: Optional[X12AN] = element(
        name="L1101",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="L1102",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    Description: Optional[X12AN] = element(
        name="L1103",
        description="Description",
        min_length=1,
        max_length=80,
    )
