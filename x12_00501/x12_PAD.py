# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PAD(Segment):
    """
    PAD - Product Adjustment Detail
    
    Description:
        To specify the product transfer type, and/or line item number
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PAD/
    """
    _id: Literal["PAD"] = id_element(name="PAD")

    AssignedIdentification: Optional[X12AN] = element(
        name="PAD01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ProductTransferTypeCode: Optional[X12ID] = element(
        name="PAD02",
        description="Product Transfer Type Code",
        min_length=2,
        max_length=2,
    )

    ChangeOrResponseTypeCode: Optional[X12ID] = element(
        name="PAD03",
        description="Change or Response Type Code",
        min_length=2,
        max_length=2,
    )

    PriceMultiplierQualifier: Optional[X12ID] = element(
        name="PAD04",
        description="Price Multiplier Qualifier",
        min_length=3,
        max_length=3,
    )

    Multiplier: Optional[X12R] = element(
        name="PAD05",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )
