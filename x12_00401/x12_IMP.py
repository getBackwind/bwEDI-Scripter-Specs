# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class IMP(Segment):
    """
    IMP - Impairment Detail
    
    Description:
        To specify impairment to a body part
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IMP/
    """
    _id: Literal["IMP"] = id_element(name="IMP")

    PartOfBodyCode: X12ID = element(
        name="IMP01",
        description="Part of Body Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Percent: Optional[X12R] = element(
        name="IMP02",
        description="Percent",
        min_length=1,
        max_length=10,
    )
