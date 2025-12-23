# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class G50(Segment):
    """
    G50 - Purchase Order Identification
    
    Description:
        To transmit identifying dates and numbers for this transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G50/
    """
    _id: Literal["G50"] = id_element(name="G50")

    OrderStatusCode: X12ID = element(
        name="G5001",
        description="Order Status Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="G5002",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    PurchaseOrderNumber: X12AN = element(
        name="G5003",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    TaxExemptCode: Optional[X12ID] = element(
        name="G5004",
        description="Tax Exempt Code",
        min_length=1,
        max_length=1,
    )

    MasterReferenceLinkNumber: Optional[X12AN] = element(
        name="G5005",
        description="Master Reference (Link) Number",
        min_length=1,
        max_length=22,
    )

    LinkSequenceNumber: Optional[X12Nn] = element(
        name="G5006",
        description="Link Sequence Number",
        min_length=6,
        max_length=6,
    )

    PurchaseOrderTypeCode: Optional[X12ID] = element(
        name="G5007",
        description="Purchase Order Type Code",
        min_length=2,
        max_length=2,
    )
