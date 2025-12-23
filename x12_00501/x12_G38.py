# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class G38(Segment):
    """
    G38 - Claim Payment Information
    
    Description:
        To indicate the payment amount and reason for disposal of unsalable product
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G38/
    """
    _id: Literal["G38"] = id_element(name="G38")

    MonetaryAmount: X12R = element(
        name="G3801",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="G3802",
        description="Payment Method Code",
        min_length=3,
        max_length=3,
    )

    ReturnsDispositionCode: Optional[X12ID] = element(
        name="G3803",
        description="Returns Disposition Code",
        min_length=2,
        max_length=2,
    )
