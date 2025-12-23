# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BLS(Segment):
    """
    BLS - Beginning Segment for Asset Schedule
    
    Description:
        To indicate the beginning of the Asset Schedule Transaction Set and transmit type of schedule and identifying numbers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BLS/
    """
    _id: Literal["BLS"] = id_element(name="BLS")

    TransactionSetPurposeCode: X12ID = element(
        name="BLS01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: X12ID = element(
        name="BLS02",
        description="Transaction Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: X12AN = element(
        name="BLS03",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BLS04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BLS05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    AcknowledgmentType: Optional[X12ID] = element(
        name="BLS06",
        description="Acknowledgment Type",
    )
