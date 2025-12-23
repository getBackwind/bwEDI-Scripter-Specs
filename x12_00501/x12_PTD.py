# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class PTD(Segment):
    """
    PTD - Product Transfer and Resale Detail
    
    Description:
        To indicate the start of detail information relating to the transfer/resale of a product and provide identifying data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PTD/
    """
    _id: Literal["PTD"] = id_element(name="PTD")

    ProductTransferTypeCode: X12ID = element(
        name="PTD01",
        description="Product Transfer Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    PriceMultiplierQualifier: Optional[X12ID] = element(
        name="PTD02",
        description="Price Multiplier Qualifier",
        min_length=3,
        max_length=3,
    )

    Multiplier: Optional[X12R] = element(
        name="PTD03",
        description="Multiplier",
        min_length=1,
        max_length=10,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="PTD04",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PTD05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ProductTransferMovementTypeCode: Optional[X12ID] = element(
        name="PTD06",
        description="Product Transfer Movement Type Code",
        min_length=2,
        max_length=2,
    )
