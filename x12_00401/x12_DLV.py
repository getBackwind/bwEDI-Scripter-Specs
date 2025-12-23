# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DLV(Segment):
    """
    DLV - Deliverable Information
    
    Description:
        To identify the product to be delivered or the service to be performed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DLV/
    """
    _id: Literal["DLV"] = id_element(name="DLV")

    QuantityOrdered: X12R = element(
        name="DLV01",
        description="Quantity Ordered",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    ProductServiceIDQualifier: Optional[X12ID] = element(
        name="DLV02",
        description="Product/Service ID Qualifier",
        min_length=2,
        max_length=2,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="DLV03",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProgramTypeCode: Optional[X12ID] = element(
        name="DLV04",
        description="Program Type Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="DLV05",
        description="Description",
        min_length=1,
        max_length=80,
    )
