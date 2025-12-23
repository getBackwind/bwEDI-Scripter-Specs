# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class FA2(Segment):
    """
    FA2 - Accounting Data
    
    Description:
        To specify the detailed accounting data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/FA2/
    """
    _id: Literal["FA2"] = id_element(name="FA2")

    BreakdownStructureDetailCode: X12ID = element(
        name="FA201",
        description="Breakdown Structure Detail Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FinancialInformationCode: X12AN = element(
        name="FA202",
        description="Financial Information Code",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
