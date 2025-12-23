# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BCQ(Segment):
    """
    BCQ - Beginning Segment for Shipper's Car Order
    
    Description:
        To indicate the beginning of the Shipper's Car Order Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BCQ/
    """
    _id: Literal["BCQ"] = id_element(name="BCQ")

    TransactionSetPurposeCode: X12ID = element(
        name="BCQ01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BCQ02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: X12TM = element(
        name="BCQ03",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BCQ04",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCQ05",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="BCQ06",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
