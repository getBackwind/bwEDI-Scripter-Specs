# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class LV(Segment):
    """
    LV - Loan Verification
    
    Description:
        To identify the specific confirmation and exception codes for loan verification
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LV/
    """
    _id: Literal["LV"] = id_element(name="LV")

    AssignedNumber: X12Nn = element(
        name="LV01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    LoanVerificationCode: X12ID = element(
        name="LV02",
        description="Loan Verification Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )
