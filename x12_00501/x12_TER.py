# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TER(Segment):
    """
    TER - Territory
    
    Description:
        To specify a territory or country, and products or services, related to a specific class of trade
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TER/
    """
    _id: Literal["TER"] = id_element(name="TER")

    ClassOfTradeCode: X12ID = element(
        name="TER01",
        description="Class of Trade Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    GeneralTerritoryCode: Optional[X12ID] = element(
        name="TER02",
        description="General Territory Code",
        min_length=1,
        max_length=2,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="TER03",
        description="Free-form Message Text",
        min_length=1,
        max_length=264,
    )

    CountryCode: Optional[X12ID] = element(
        name="TER04",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="TER05",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    FreeFormMessageText2: Optional[X12AN] = element(
        name="TER06",
        description="Free-form Message Text",
        min_length=1,
        max_length=264,
    )
