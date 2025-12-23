# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class TII(Segment):
    """
    TII - Tax Installment Information
    
    Description:
        To provide the information on real estate taxes, including amounts
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TII/
    """
    _id: Literal["TII"] = id_element(name="TII")

    YesNoConditionOrResponseCode: X12ID = element(
        name="TII01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Quantity: X12R = element(
        name="TII02",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    MonetaryAmount: X12R = element(
        name="TII03",
        description="Monetary Amount",
        mandatory=True,
        min_length=1,
        max_length=18,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="TII04",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    TaxServiceNonPaymentCode: Optional[X12ID] = element(
        name="TII05",
        description="Tax Service Non-payment Code",
        min_length=1,
        max_length=3,
    )
