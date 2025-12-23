# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class LUC(Segment):
    """
    LUC - Loan Underwriting
    
    Description:
        To identify the loan underwriting codes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LUC/
    """
    _id: Literal["LUC"] = id_element(name="LUC")

    LoanDocumentationTypeCode: X12ID = element(
        name="LUC01",
        description="Loan Documentation Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    LoanPurposeCode: X12ID = element(
        name="LUC02",
        description="Loan Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    RiskOfLossCode: Optional[X12ID] = element(
        name="LUC04",
        description="Risk of Loss Code",
        min_length=2,
        max_length=2,
    )
