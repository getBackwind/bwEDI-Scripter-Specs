# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BQT(Segment):
    """
    BQT - Beginning Segment for Request for Quotation
    
    Description:
        To indicate the beginning of a Request for Quotation Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BQT/
    """
    _id: Literal["BQT"] = id_element(name="BQT")

    TransactionSetPurposeCode: X12ID = element(
        name="BQT01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RequestForQuoteReferenceNumber: X12AN = element(
        name="BQT02",
        description="Request for Quote Reference Number",
        mandatory=True,
        min_length=1,
        max_length=45,
    )

    Date: X12DT = element(
        name="BQT03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="BQT04",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="BQT05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PurchaseOrderTypeCode: Optional[X12ID] = element(
        name="BQT06",
        description="Purchase Order Type Code",
        min_length=2,
        max_length=2,
    )

    RequestForQuoteTypeCode: Optional[X12ID] = element(
        name="BQT07",
        description="Request for Quote Type Code",
        min_length=2,
        max_length=2,
    )

    ContractTypeCode: Optional[X12ID] = element(
        name="BQT08",
        description="Contract Type Code",
        min_length=2,
        max_length=2,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BQT09",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    PurchaseCategory: Optional[X12ID] = element(
        name="BQT10",
        description="Purchase Category",
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="BQT11",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )
