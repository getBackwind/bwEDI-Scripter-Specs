# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BSF(Segment):
    """
    BSF - Business Function
    
    Description:
        To transmit basic data identifying the function performed at a facility
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BSF/
    """
    _id: Literal["BSF"] = id_element(name="BSF")

    ClassOfTradeCode: Optional[X12ID] = element(
        name="BSF01",
        description="Class of Trade Code",
        min_length=2,
        max_length=2,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="BSF02",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="BSF03",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
