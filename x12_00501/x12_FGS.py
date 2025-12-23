# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class FGS(Segment):
    """
    FGS - Form Group
    
    Description:
        To provide information for a section or data group in a form or schedule
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FGS/
    """
    _id: Literal["FGS"] = id_element(name="FGS")

    AssignedIdentification: X12AN = element(
        name="FGS01",
        description="Assigned Identification",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="FGS02",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="FGS03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
