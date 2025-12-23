# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class PUN(Segment):
    """
    PUN - Beginning Segment for Motor Carrier Pickup Notification
    
    Description:
        To transmit identifying numbers and other basic data relating to the Motor Carrier Pickup Notification transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PUN/
    """
    _id: Literal["PUN"] = id_element(name="PUN")

    StandardCarrierAlphaCode: X12ID = element(
        name="PUN01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Date: X12DT = element(
        name="PUN02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="PUN03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="PUN04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Time2: Optional[X12TM] = element(
        name="PUN05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TransactionSetPurposeCode: X12ID = element(
        name="PUN06",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )
