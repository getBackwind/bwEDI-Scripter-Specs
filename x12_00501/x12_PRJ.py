# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class PRJ(Segment):
    """
    PRJ - Multifamily Housing Project
    
    Description:
        To describe attributes of a multifamily housing project
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PRJ/
    """
    _id: Literal["PRJ"] = id_element(name="PRJ")

    Name: X12AN = element(
        name="PRJ01",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="PRJ02",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PRJ03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date: Optional[X12DT] = element(
        name="PRJ04",
        description="Date",
        min_length=8,
        max_length=8,
    )
