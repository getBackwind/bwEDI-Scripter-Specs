# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BQR(Segment):
    """
    BQR - Beginning Segment for Response to Request for Quotation
    
    Description:
        To indicate the beginning of a Response to Request for Quote Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BQR/
    """
    _id: Literal["BQR"] = id_element(name="BQR")

    TransactionSetPurposeCode: X12ID = element(
        name="BQR01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RequestForQuoteReferenceNumber: X12AN = element(
        name="BQR02",
        description="Request for Quote Reference Number",
        mandatory=True,
        min_length=1,
        max_length=45,
    )

    Date: X12DT = element(
        name="BQR03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="BQR04",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date2: Optional[X12DT] = element(
        name="BQR05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    BidTypeResponseCode: Optional[X12ID] = element(
        name="BQR06",
        description="Bid Type Response Code",
        min_length=2,
        max_length=2,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BQR07",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )

    ChangeOrderSequenceNumber: Optional[X12AN] = element(
        name="BQR08",
        description="Change Order Sequence Number",
        min_length=1,
        max_length=8,
    )
