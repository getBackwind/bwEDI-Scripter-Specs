# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class F05(Segment):
    """
    F05 - Allowance/Charge (Claim)
    
    Description:
        To report allowances or charges relative to a shipment against which a claim is made
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/F05/
    """
    _id: Literal["F05"] = id_element(name="F05")

    ChargeAllowanceQualifier: X12ID = element(
        name="F0501",
        description="Charge/Allowance Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Amount: X12Nn = element(
        name="F0502",
        description="Amount",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    CreditDebitFlagCode: X12ID = element(
        name="F0503",
        description="Credit/Debit Flag Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )
