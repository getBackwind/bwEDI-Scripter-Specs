# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BCH(Segment):
    """
    BCH - Beginning Segment for Purchase Order Change
    
    Description:
        To indicate the beginning of the Purchase Order Change Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BCH/
    """
    _id: Literal["BCH"] = id_element(name="BCH")

    TransactionSetPurposeCode: X12ID = element(
        name="BCH01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    PurchaseOrderTypeCode: X12ID = element(
        name="BCH02",
        description="Purchase Order Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    PurchaseOrderNumber: X12AN = element(
        name="BCH03",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="BCH04",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="BCH05",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )

    Date: X12DT = element(
        name="BCH06",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    RequestReferenceNumber: Optional[X12AN] = element(
        name="BCH07",
        description="Request Reference Number",
        min_length=1,
        max_length=45,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BCH08",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCH09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date2: Optional[X12DT] = element(
        name="BCH10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date3: Optional[X12DT] = element(
        name="BCH11",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="BCH12",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BCH13",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    AcknowledgmentType: Optional[X12ID] = element(
        name="BCH14",
        description="Acknowledgment Type",
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BCH15",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    PurchaseCategory: Optional[X12ID] = element(
        name="BCH16",
        description="Purchase Category",
    )
