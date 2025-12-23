# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class PRF(Segment):
    """
    PRF - Purchase Order Reference
    
    Description:
        To provide reference to a specific purchase order
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PRF/
    """
    _id: Literal["PRF"] = id_element(name="PRF")

    OrderID: X12AN = element(
        name="PRF01",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="PRF02",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="PRF03",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )

    Date: Optional[X12DT] = element(
        name="PRF04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AssignedIdentification: Optional[X12AN] = element(
        name="PRF05",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    ContractNumber: Optional[X12AN] = element(
        name="PRF06",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    PurchaseOrderTypeCode: Optional[X12ID] = element(
        name="PRF07",
        description="Purchase Order Type Code",
        min_length=2,
        max_length=2,
    )
