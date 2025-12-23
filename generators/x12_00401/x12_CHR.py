# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class CHR(Segment):
    """
    CHR - Car Hire Rates
    
    Description:
        To identify source and type of car hire rate
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CHR/
    """
    _id: Literal["CHR"] = id_element(name="CHR")

    RateSource: X12ID = element(
        name="CHR01",
        description="Rate Source",
        mandatory=True,
    )

    BilledRatedAsQualifier: X12ID = element(
        name="CHR02",
        description="Billed/Rated-as Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Multiplier: Optional[X12R] = element(
        name="CHR03",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )
