# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class JID(Segment):
    """
    JID - Equipment Detail
    
    Description:
        To specify equipment charged within a particular service code
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/JID/
    """
    _id: Literal["JID"] = id_element(name="JID")

    ProductServiceIDQualifier: X12ID = element(
        name="JID01",
        description="Product/Service ID Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProductServiceID: X12AN = element(
        name="JID02",
        description="Product/Service ID",
        mandatory=True,
        min_length=1,
        max_length=48,
    )

    Quantity: Optional[X12R] = element(
        name="JID03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    ProductServiceConditionCode: Optional[X12ID] = element(
        name="JID05",
        description="Product/Service Condition Code",
        min_length=2,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="JID06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )
