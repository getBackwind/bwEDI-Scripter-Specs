# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn, X12R


class G84(Segment):
    """
    G84 - Delivery/Return Record of Totals
    
    Description:
        To specify summary details of total items in terms of quantity or amount
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/G84/
    """
    _id: Literal["G84"] = id_element(name="G84")

    Quantity: Optional[X12R] = element(
        name="G8401",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    TotalInvoiceAmount: Optional[X12Nn] = element(
        name="G8402",
        description="Total Invoice Amount",
        min_length=1,
        max_length=10,
    )

    TotalDepositDollarAmount: Optional[X12Nn] = element(
        name="G8403",
        description="Total Deposit Dollar Amount",
        min_length=1,
        max_length=6,
    )
