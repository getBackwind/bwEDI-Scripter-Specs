# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class Q7(Segment):
    """
    Q7 - Lading Exception Status
    
    Description:
        To specify the status of the shipment in terms of lading exception information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/Q7/
    """
    _id: Literal["Q7"] = id_element(name="Q7")

    LadingExceptionCode: X12ID = element(
        name="Q701",
        description="Lading Exception Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    PackagingFormCode: Optional[X12ID] = element(
        name="Q702",
        description="Packaging Form Code",
        min_length=3,
        max_length=3,
    )

    LadingQuantity: Optional[X12Nn] = element(
        name="Q703",
        description="Lading Quantity",
        min_length=1,
        max_length=7,
    )
