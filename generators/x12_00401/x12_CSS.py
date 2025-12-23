# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class CSS(Segment):
    """
    CSS - Conditional Sampling Sequence
    
    Description:
        To specify a special sample-selection procedure to be followed at the start-up of a process, or following a process upset, such as a brief line power loss or product grade change
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CSS/
    """
    _id: Literal["CSS"] = id_element(name="CSS")

    SamplingSequenceQualifier: X12ID = element(
        name="CSS01",
        description="Sampling Sequence Qualifier",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    SamplingSequenceValue: X12Nn = element(
        name="CSS03",
        description="Sampling Sequence Value",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    SamplingSequenceValue2: Optional[X12Nn] = element(
        name="CSS04",
        description="Sampling Sequence Value",
        min_length=1,
        max_length=3,
    )

    SamplingSequenceValue3: Optional[X12Nn] = element(
        name="CSS05",
        description="Sampling Sequence Value",
        min_length=1,
        max_length=3,
    )

    SamplingSequenceValue4: Optional[X12Nn] = element(
        name="CSS06",
        description="Sampling Sequence Value",
        min_length=1,
        max_length=3,
    )

    SamplingSequenceValue5: Optional[X12Nn] = element(
        name="CSS07",
        description="Sampling Sequence Value",
        min_length=1,
        max_length=3,
    )
