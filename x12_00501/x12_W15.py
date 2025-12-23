# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class W15(Segment):
    """
    W15 - Warehouse Adjustment Identification
    
    Description:
        To provide identifying numbers and dates and other basic data for this transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W15/
    """
    _id: Literal["W15"] = id_element(name="W15")

    Date: X12DT = element(
        name="W1501",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    AdjustmentNumber: Optional[X12AN] = element(
        name="W1502",
        description="Adjustment Number",
        min_length=1,
        max_length=22,
    )

    AdjustmentNumber2: Optional[X12AN] = element(
        name="W1503",
        description="Adjustment Number",
        min_length=1,
        max_length=22,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="W1504",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="W1505",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )

    ActionCode: Optional[X12ID] = element(
        name="W1506",
        description="Action Code",
        min_length=1,
        max_length=2,
    )
