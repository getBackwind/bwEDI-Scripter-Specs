# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BAK(Segment):
    """
    BAK - Beginning Segment for Purchase Order Acknowledgment
    
    Description:
        To indicate the beginning of the Purchase Order Acknowledgment Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BAK/
    """
    _id: Literal["BAK"] = id_element(name="BAK")

    TransactionSetPurpose: X12ID = element(
        name="BAK01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Acknowledgment: X12ID = element(
        name="BAK02",
        description="Acknowledgment Type",
        mandatory=True,
    )

    PurchaseOrderID: X12AN = element(
        name="BAK03",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    PurchaseOrderDate: X12DT = element(
        name="BAK04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="BAK05",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    RequestReferenceNumber: Optional[X12AN] = element(
        name="BAK06",
        description="Request Reference Number",
        min_length=1,
        max_length=45,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BAK07",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    ReferenceID: Optional[X12AN] = element(
        name="BAK08",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    AcknowledgmentDate: Optional[X12DT] = element(
        name="BAK09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BAK10",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
