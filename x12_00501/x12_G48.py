# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class G48(Segment):
    """
    G48 - Statement/Invoice Identification
    
    Description:
        To uniquely identify an invoice or adjustment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G48/
    """
    _id: Literal["G48"] = id_element(name="G48")

    InvoiceNumber: Optional[X12AN] = element(
        name="G4801",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    Date: Optional[X12DT] = element(
        name="G4802",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StoreNumber: Optional[X12AN] = element(
        name="G4803",
        description="Store Number",
        min_length=1,
        max_length=10,
    )

    Date2: Optional[X12DT] = element(
        name="G4804",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="G4805",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    VendorOrderNumber: Optional[X12AN] = element(
        name="G4806",
        description="Vendor Order Number",
        min_length=1,
        max_length=22,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="G4807",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="G4808",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date3: Optional[X12DT] = element(
        name="G4809",
        description="Date",
        min_length=8,
        max_length=8,
    )
