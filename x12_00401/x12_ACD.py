# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class ACD(Segment):
    """
    ACD - Account Description
    
    Description:
        To specify type of relationship between entity and vendor or financial institution
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ACD/
    """
    _id: Literal["ACD"] = id_element(name="ACD")

    AccountRelationshipCode: Optional[X12ID] = element(
        name="ACD01",
        description="Account Relationship Code",
        min_length=1,
        max_length=1,
    )

    RatingRemarksCode: Optional[X12ID] = element(
        name="ACD02",
        description="Rating Remarks Code",
        min_length=2,
        max_length=2,
    )

    LoanTypeCode: Optional[X12ID] = element(
        name="ACD03",
        description="Loan Type Code",
        min_length=1,
        max_length=2,
    )
