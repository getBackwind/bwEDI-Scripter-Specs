# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class LHR(Segment):
    """
    LHR - Hazardous Material Identifying Reference Numbers
    
    Description:
        To transmit specific hazardous material reference numbers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LHR/
    """
    _id: Literal["LHR"] = id_element(name="LHR")

    ReferenceIdentificationQualifier: X12ID = element(
        name="LHR01",
        description="Reference Identification Qualifier",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: X12AN = element(
        name="LHR02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    Date: Optional[X12DT] = element(
        name="LHR03",
        description="Date",
        min_length=8,
        max_length=8,
    )
