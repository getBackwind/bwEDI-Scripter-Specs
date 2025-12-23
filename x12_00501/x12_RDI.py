# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class RDI(Segment):
    """
    RDI - Retail Account Demographic Information
    
    Description:
        To report demographic information regarding a retail account
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RDI/
    """
    _id: Literal["RDI"] = id_element(name="RDI")

    EntityIdentifierCode: X12ID = element(
        name="RDI01",
        description="Entity Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=3,
    )

    CountryCode: Optional[X12ID] = element(
        name="RDI02",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="RDI03",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )

    Amount: Optional[X12Nn] = element(
        name="RDI04",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Description: Optional[X12AN] = element(
        name="RDI05",
        description="Description",
        min_length=1,
        max_length=80,
    )
