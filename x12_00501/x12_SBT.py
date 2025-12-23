# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SBT(Segment):
    """
    SBT - Subtest
    
    Description:
        To provide information about subtests that the student has taken
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SBT/
    """
    _id: Literal["SBT"] = id_element(name="SBT")

    SubtestCode: X12ID = element(
        name="SBT01",
        description="Subtest Code",
        mandatory=True,
        min_length=5,
        max_length=5,
    )

    Name: Optional[X12AN] = element(
        name="SBT02",
        description="Name",
        min_length=1,
        max_length=60,
    )

    TestScoreInterpretationCode: Optional[X12ID] = element(
        name="SBT03",
        description="Test Score Interpretation Code",
        min_length=1,
        max_length=1,
    )
