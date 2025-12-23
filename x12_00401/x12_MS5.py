# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class MS5(Segment):
    """
    MS5 - Shipment Rates and Charges
    
    Description:
        To specify shipment rates and charges
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MS5/
    """
    _id: Literal["MS5"] = id_element(name="MS5")

    DeclaredValue: Optional[X12Nn] = element(
        name="MS501",
        description="Declared Value",
        min_length=2,
        max_length=12,
    )

    RateValueQualifier: Optional[X12ID] = element(
        name="MS502",
        description="Rate/Value Qualifier",
        min_length=2,
        max_length=2,
    )

    FreightRate: Optional[X12R] = element(
        name="MS503",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    DeclaredValue2: Optional[X12Nn] = element(
        name="MS504",
        description="Declared Value",
        min_length=2,
        max_length=12,
    )

    CurrencyCode: Optional[X12ID] = element(
        name="MS505",
        description="Currency Code",
        min_length=3,
        max_length=3,
    )
