# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class ASM(Segment):
    """
    ASM - Amount and Settlement Method
    
    Description:
        To Complete Performance Index (TCPI) for Budget at Complete (BAC)
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ASM/
    """
    _id: Literal["ASM"] = id_element(name="ASM")

    Amount: X12Nn = element(
        name="ASM01",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    PaymentMethodTypeCode: Optional[X12ID] = element(
        name="ASM02",
        description="Payment Method Type Code",
        min_length=1,
        max_length=2,
    )

    AmountQualifierCode: Optional[X12ID] = element(
        name="ASM03",
        description="Amount Qualifier Code",
        min_length=1,
        max_length=3,
    )
