# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BIG(Segment):
    """
    BIG - Beginning Segment for Invoice
    
    Description:
        To indicate the beginning of an invoice transaction set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BIG/
    """
    _id: Literal["BIG"] = id_element(name="BIG")

    InvoiceDate: X12DT = element(
        name="BIG01",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    InvoiceID: X12AN = element(
        name="BIG02",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    PurchaseOrderDate: Optional[X12DT] = element(
        name="BIG03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderID: Optional[X12AN] = element(
        name="BIG04",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="BIG05",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="BIG06",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )

    TransactionType: Optional[X12ID] = element(
        name="BIG07",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BIG08",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BIG09",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="BIG10",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )
