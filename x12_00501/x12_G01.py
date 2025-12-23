# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class G01(Segment):
    """
    G01 - Invoice Identification
    
    Description:
        To transmit identifying dates and numbers for this transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G01/
    """
    _id: Literal["G01"] = id_element(name="G01")

    Date: X12DT = element(
        name="G0101",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    InvoiceNumber: X12AN = element(
        name="G0102",
        description="Invoice Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    Date2: Optional[X12DT] = element(
        name="G0103",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="G0104",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    VendorOrderNumber: Optional[X12AN] = element(
        name="G0105",
        description="Vendor Order Number",
        min_length=1,
        max_length=22,
    )

    MasterReferenceLinkNumber: Optional[X12AN] = element(
        name="G0106",
        description="Master Reference (Link) Number",
        min_length=1,
        max_length=22,
    )

    LinkSequenceNumber: Optional[X12Nn] = element(
        name="G0107",
        description="Link Sequence Number",
        min_length=6,
        max_length=6,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="G0108",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
