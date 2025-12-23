# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class PCR(Segment):
    """
    PCR - Payment Cancellation Request
    
    Description:
        To identify cancellation type and amount
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PCR/
    """
    _id: Literal["PCR"] = id_element(name="PCR")

    PaymentCancellationType: X12ID = element(
        name="PCR01",
        description="Payment Cancellation Type",
        mandatory=True,
    )

    MonetaryAmount: X12R = element(
        name="PCR02",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )
