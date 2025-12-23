# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BC(Segment):
    """
    BC - Beginning Segment for Contract Completion Status
    
    Description:
        To indicate the beginning of a Contract Completion Status Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BC/
    """
    _id: Literal["BC"] = id_element(name="BC")

    TransactionSetPurposeCode: X12ID = element(
        name="BC01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="BC02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BC03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BC04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BC05",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BC06",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BC07",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
