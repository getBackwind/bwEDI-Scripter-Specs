# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class XQ(Segment):
    """
    XQ - Reporting Date/Action
    
    Description:
        To specify reporting date and action to be taken
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/XQ/
    """
    _id: Literal["XQ"] = id_element(name="XQ")

    TransactionHandlingCode: X12ID = element(
        name="XQ01",
        description="Transaction Handling Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Date: X12DT = element(
        name="XQ02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="XQ03",
        description="Date",
        min_length=8,
        max_length=8,
    )
