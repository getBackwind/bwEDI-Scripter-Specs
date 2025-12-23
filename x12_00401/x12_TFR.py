# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TFR(Segment):
    """
    TFR - Tariff Restrictions
    
    Description:
        To define tariff restrictions values such as charges, mileage and weight
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TFR/
    """
    _id: Literal["TFR"] = id_element(name="TFR")

    TariffRestrictionIDCode: X12ID = element(
        name="TFR01",
        description="Tariff Restriction ID Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    TariffRestrictionDescription: Optional[X12AN] = element(
        name="TFR02",
        description="Tariff Restriction Description",
        min_length=1,
        max_length=10,
    )

    TariffRestrictionValue: Optional[X12R] = element(
        name="TFR03",
        description="Tariff Restriction Value",
        min_length=1,
        max_length=9,
    )

    TariffRestrictionValue2: Optional[X12R] = element(
        name="TFR04",
        description="Tariff Restriction Value",
        min_length=1,
        max_length=9,
    )
