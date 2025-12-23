# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class UWI(Segment):
    """
    UWI - Underwriting Information
    
    Description:
        To identify the type of underwriting used to underwrite a mortgage loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/UWI/
    """
    _id: Literal["UWI"] = id_element(name="UWI")

    UnderwritingMethodCode: X12ID = element(
        name="UWI01",
        description="Underwriting Method Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Name: Optional[X12AN] = element(
        name="UWI02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    DispositionCode: Optional[X12ID] = element(
        name="UWI03",
        description="Disposition Code",
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="UWI04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
