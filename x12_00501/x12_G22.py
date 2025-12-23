# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class G22(Segment):
    """
    G22 - Pre-Pricing Information
    
    Description:
        To specify pre-pricing information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G22/
    """
    _id: Literal["G22"] = id_element(name="G22")

    PrePricedOptionCode: X12ID = element(
        name="G2201",
        description="Pre-priced Option Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PriceNewSuggestedRetail: Optional[X12Nn] = element(
        name="G2202",
        description="Price New, Suggested Retail",
        min_length=2,
        max_length=7,
    )

    MultiplePriceQuantity: Optional[X12Nn] = element(
        name="G2203",
        description="Multiple Price Quantity",
        min_length=1,
        max_length=2,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="G2204",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )

    Date: Optional[X12DT] = element(
        name="G2205",
        description="Date",
        min_length=8,
        max_length=8,
    )
