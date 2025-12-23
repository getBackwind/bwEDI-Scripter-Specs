# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12R


class MCD(Segment):
    """
    MCD - Mortgage Closing Data
    
    Description:
        To provide details about loan settlement
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MCD/
    """
    _id: Literal["MCD"] = id_element(name="MCD")

    MonetaryAmount: X12R = element(
        name="MCD01",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    Date: Optional[X12DT] = element(
        name="MCD02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="MCD03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Name: Optional[X12AN] = element(
        name="MCD04",
        description="Name",
        min_length=1,
        max_length=60,
    )
