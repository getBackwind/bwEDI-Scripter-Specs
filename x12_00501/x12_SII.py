# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SII(Segment):
    """
    SII - Sales Item Information
    
    Description:
        To specify line item information related to a sale of an item
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SII/
    """
    _id: Literal["SII"] = id_element(name="SII")

    ProductServiceIDQualifier: X12ID = element(
        name="SII01",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="SII02",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    Quantity: X12R = element(
        name="SII03",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitPrice: Optional[X12R] = element(
        name="SII05",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    UnitPrice2: Optional[X12R] = element(
        name="SII06",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="SII07",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
