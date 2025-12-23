# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn


class TDS(Segment):
    """
    TDS - Total Monetary Value Summary
    
    Description:
        To specify the total invoice discounts and amounts
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TDS/
    """
    _id: Literal["TDS"] = id_element(name="TDS")

    TotalAmount: X12Nn = element(
        name="TDS01",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Amount: Optional[X12Nn] = element(
        name="TDS02",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount2: Optional[X12Nn] = element(
        name="TDS03",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    Amount3: Optional[X12Nn] = element(
        name="TDS04",
        description="Amount",
        min_length=1,
        max_length=15,
    )
