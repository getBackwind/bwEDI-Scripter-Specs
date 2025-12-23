# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class RH(Segment):
    """
    RH - Personal Property Rate
    
    Description:
        To specify the rate for a personal property/household goods service
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/RH/
    """
    _id: Literal["RH"] = id_element(name="RH")

    TariffServiceCode: Optional[X12ID] = element(
        name="RH01",
        description="Tariff Service Code",
        min_length=2,
        max_length=2,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="RH02",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    FreightRate: Optional[X12R] = element(
        name="RH03",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )
