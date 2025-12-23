# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class STC(Segment):
    """
    STC - Status Information
    
    Description:
        To report the status, required action, and paid information of a claim or service line
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/STC/
    """
    _id: Literal["STC"] = id_element(name="STC")

    Date: Optional[X12DT] = element(
        name="STC02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ActionCode: Optional[X12ID] = element(
        name="STC03",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="STC04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="STC05",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Date2: Optional[X12DT] = element(
        name="STC06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="STC07",
        description="Payment Method Code",
        min_length=3,
        max_length=3,
    )

    Date3: Optional[X12DT] = element(
        name="STC08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    CheckNumber: Optional[X12AN] = element(
        name="STC09",
        description="Check Number",
        min_length=1,
        max_length=16,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="STC12",
        description="Free-form Message Text",
        min_length=1,
        max_length=264,
    )
