# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class BGN(Segment):
    """
    BGN - Beginning Segment
    
    Description:
        To indicate the beginning of a transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BGN/
    """
    _id: Literal["BGN"] = id_element(name="BGN")

    PurposeCode: X12ID = element(
        name="BGN01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceID: X12AN = element(
        name="BGN02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="BGN03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="BGN04",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="BGN05",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BGN06",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="BGN07",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="BGN08",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    SecurityLevelCode: Optional[X12ID] = element(
        name="BGN09",
        description="Security Level Code",
        min_length=2,
        max_length=2,
    )
