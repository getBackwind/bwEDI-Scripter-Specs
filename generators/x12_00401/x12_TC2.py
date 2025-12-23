# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class TC2(Segment):
    """
    TC2 - Commodity
    
    Description:
        To identify a commodity or a group of commodities or a tariff page commodity
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TC2/
    """
    _id: Literal["TC2"] = id_element(name="TC2")

    CommodityCodeQualifier: X12ID = element(
        name="TC201",
        description="Commodity Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CommodityCode: X12AN = element(
        name="TC202",
        description="Commodity Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )
