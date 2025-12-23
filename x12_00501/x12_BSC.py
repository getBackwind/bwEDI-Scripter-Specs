# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class BSC(Segment):
    """
    BSC - Beginning Segment for Commission Sales Report and Periodic Compensation
    
    Description:
        To indicate the beginning of a commission sales report or periodic compensation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BSC/
    """
    _id: Literal["BSC"] = id_element(name="BSC")

    TransactionSetPurposeCode: X12ID = element(
        name="BSC01",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="BSC02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: X12DT = element(
        name="BSC03",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date3: X12DT = element(
        name="BSC04",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )
