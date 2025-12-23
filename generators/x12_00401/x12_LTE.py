# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LTE(Segment):
    """
    LTE - Letter of Recommendation Evaluation
    
    Description:
        To provide evaluation information as part of a letter of recommendation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LTE/
    """
    _id: Literal["LTE"] = id_element(name="LTE")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="LTE01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="LTE02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="LTE03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    RatingSummaryValueCode: Optional[X12ID] = element(
        name="LTE04",
        description="Rating Summary Value Code",
        min_length=1,
        max_length=2,
    )
