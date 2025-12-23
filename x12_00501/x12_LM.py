# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LM(Segment):
    """
    LM - Code Source Information
    
    Description:
        To transmit standard code list identification information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LM/
    """
    _id: Literal["LM"] = id_element(name="LM")

    AgencyQualifierCode: X12ID = element(
        name="LM01",
        description="Agency Qualifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    SourceSubqualifier: Optional[X12AN] = element(
        name="LM02",
        description="Source Subqualifier",
        min_length=1,
        max_length=15,
    )
