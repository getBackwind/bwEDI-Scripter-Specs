# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CLR(Segment):
    """
    CLR - Car Location Routing Request
    
    Description:
        To identify the network address of parties to receive notification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CLR/
    """
    _id: Literal["CLR"] = id_element(name="CLR")

    IdentificationCodeQualifier: X12ID = element(
        name="CLR01",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="CLR02",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    IndustryCode: Optional[X12AN] = element(
        name="CLR03",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CLR04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
