# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class G63(Segment):
    """
    G63 - Period
    
    Description:
        To define the billing periods
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G63/
    """
    _id: Literal["G63"] = id_element(name="G63")

    TimePeriodQualifier: X12ID = element(
        name="G6301",
        description="Time Period Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    NumberOfPeriods: X12Nn = element(
        name="G6302",
        description="Number of Periods",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    TariffApplicationCode: Optional[X12ID] = element(
        name="G6303",
        description="Tariff Application Code",
        min_length=1,
        max_length=1,
    )

    Description: Optional[X12AN] = element(
        name="G6304",
        description="Description",
        min_length=1,
        max_length=80,
    )
