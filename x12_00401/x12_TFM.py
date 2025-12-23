# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12R


class TFM(Segment):
    """
    TFM - Tariff Minimum Rates
    
    Description:
        To transmit tariff minimum rate values
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TFM/
    """
    _id: Literal["TFM"] = id_element(name="TFM")

    FreightRate: X12R = element(
        name="TFM01",
        description="Freight Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )
