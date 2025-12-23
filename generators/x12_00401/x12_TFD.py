# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class TFD(Segment):
    """
    TFD - Tariff Adjustments Minimum Charge
    
    Description:
        To transmit tariff adjustment values for previously defined minimums
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TFD/
    """
    _id: Literal["TFD"] = id_element(name="TFD")

    RateValueQualifier: X12ID = element(
        name="TFD01",
        description="Rate/Value Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TariffAdjustmentValueAmount: X12R = element(
        name="TFD02",
        description="Tariff Adjustment Value/Amount",
        mandatory=True,
        min_length=1,
        max_length=9,
    )
