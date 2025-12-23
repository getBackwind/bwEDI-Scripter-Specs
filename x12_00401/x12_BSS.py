# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BSS(Segment):
    """
    BSS - Beginning Segment for Shipping Schedule/Production Sequence
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BSS/
    """
    _id: Literal["BSS"] = id_element(name="BSS")

    TransactionSetPurposeCode: X12ID = element(
        name="BSS01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="BSS02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BSS03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ScheduleTypeQualifier: X12ID = element(
        name="BSS04",
        description="Schedule Type Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date2: X12DT = element(
        name="BSS05",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date3: X12DT = element(
        name="BSS06",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="BSS07",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BSS08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BSS09",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    PurchaseOrderNumber: Optional[X12AN] = element(
        name="BSS10",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    ScheduleQuantityQualifier: Optional[X12ID] = element(
        name="BSS11",
        description="Schedule Quantity Qualifier",
        min_length=1,
        max_length=1,
    )
