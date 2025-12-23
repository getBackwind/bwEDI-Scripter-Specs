# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BCA(Segment):
    """
    BCA - Beginning Segment for Purchase Order Change Acknowledgment
    
    Description:
        To indicate the beginning of the Purchase Order Change Acknowledgment Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BCA/
    """
    _id: Literal["BCA"] = id_element(name="BCA")

    TransactionSetPurposeCode: X12ID = element(
        name="BCA01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AcknowledgmentType: Optional[X12ID] = element(
        name="BCA02",
        description="Acknowledgment Type",
    )

    PurchaseOrderNumber: X12AN = element(
        name="BCA03",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="BCA04",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="BCA05",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )

    Date: X12DT = element(
        name="BCA06",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    RequestReferenceNumber: Optional[X12AN] = element(
        name="BCA07",
        description="Request Reference Number",
        min_length=1,
        max_length=45,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BCA08",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCA09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date2: Optional[X12DT] = element(
        name="BCA10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: Optional[X12DT] = element(
        name="BCA11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date4: Optional[X12DT] = element(
        name="BCA12",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderTypeCode: Optional[X12ID] = element(
        name="BCA13",
        description="Purchase Order Type Code",
        min_length=2,
        max_length=2,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BCA14",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BCA15",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
