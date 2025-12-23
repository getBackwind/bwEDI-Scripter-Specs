# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class PCT(Segment):
    """
    PCT - Percent Amounts
    
    Description:
        To qualify percent amounts and supply percent amounts
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PCT/
    """
    _id: Literal["PCT"] = id_element(name="PCT")

    PercentQualifier: X12ID = element(
        name="PCT01",
        description="Percent Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    Percent: X12R = element(
        name="PCT02",
        description="Percent",
        mandatory=True,
        min_length=1,
        max_length=10,
    )
