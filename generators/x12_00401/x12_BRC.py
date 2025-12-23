# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BRC(Segment):
    """
    BRC - Beginning Segment for Response to Product Transfer Account Adjustment
    
    Description:
        To identify the beginning of a Response to Product Transfer Account Adjustment Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BRC/
    """
    _id: Literal["BRC"] = id_element(name="BRC")

    TransactionSetPurposeCode: X12ID = element(
        name="BRC01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BRC02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ReferenceIdentificationQualifier: Optional[X12ID] = element(
        name="BRC03",
        description="Reference Identification Qualifier",
        min_length=2,
        max_length=3,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BRC04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    Time: Optional[X12TM] = element(
        name="BRC05",
        description="Time",
        min_length=4,
        max_length=8,
    )
