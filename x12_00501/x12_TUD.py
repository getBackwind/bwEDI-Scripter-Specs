# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TUD(Segment):
    """
    TUD - Trade Union Data
    
    Description:
        To allow for the identification of trade union data related to a specific location or product line
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TUD/
    """
    _id: Literal["TUD"] = id_element(name="TUD")

    TradeUnionCode: X12ID = element(
        name="TUD01",
        description="Trade Union Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="TUD02",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="TUD03",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
