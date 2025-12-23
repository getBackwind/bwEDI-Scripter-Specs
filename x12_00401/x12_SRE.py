# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SRE(Segment):
    """
    SRE - Test Scores
    
    Description:
        To provide scores on tests that a student has taken
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SRE/
    """
    _id: Literal["SRE"] = id_element(name="SRE")

    TestScoreQualifierCode: X12ID = element(
        name="SRE01",
        description="Test Score Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Description: X12AN = element(
        name="SRE02",
        description="Description",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
