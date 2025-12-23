# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class B3A(Segment):
    """
    B3A - Invoice Type
    
    Description:
        To indicate type of invoice and number of shipments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/B3A/
    """
    _id: Literal["B3A"] = id_element(name="B3A")

    TransactionTypeCode: X12ID = element(
        name="B3A01",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    NumberOfShipments: Optional[X12Nn] = element(
        name="B3A02",
        description="Number of Shipments",
        min_length=1,
        max_length=5,
    )
