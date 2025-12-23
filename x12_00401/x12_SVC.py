# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12R


class SVC(Segment):
    """
    SVC - Service Information
    
    Description:
        To supply payment and control information to a provider for a particular service
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SVC/
    """
    _id: Literal["SVC"] = id_element(name="SVC")

    MonetaryAmount: X12R = element(
        name="SVC02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="SVC03",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="SVC04",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    Quantity: Optional[X12R] = element(
        name="SVC05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="SVC07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
