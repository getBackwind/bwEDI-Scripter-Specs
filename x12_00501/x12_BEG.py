# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BEG(Segment):
    """
    BEG - Beginning Segment for Purchase Order
    
    Description:
        To indicate the beginning of the Purchase Order Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BEG/
    """
    _id: Literal["BEG"] = id_element(name="BEG")

    PurposeCode: X12ID = element(
        name="BEG01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TypeCode: X12ID = element(
        name="BEG02",
        description="Purchase Order Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    PurchaseOrderNumber: X12AN = element(
        name="BEG03",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    ReleaseNumber: Optional[X12AN] = element(
        name="BEG04",
        description="Release Number",
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BEG05",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ContractNumber: Optional[X12AN] = element(
        name="BEG06",
        description="Contract Number",
        min_length=1,
        max_length=30,
    )

    AcknowledgmentType: Optional[X12ID] = element(
        name="BEG07",
        description="Acknowledgment Type",
    )

    InvoiceTypeCode: Optional[X12ID] = element(
        name="BEG08",
        description="Invoice Type Code",
        min_length=3,
        max_length=3,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="BEG09",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )

    PurchaseCategory: Optional[X12ID] = element(
        name="BEG10",
        description="Purchase Category",
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BEG11",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BEG12",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
