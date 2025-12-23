# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn, X12R


class SPS(Segment):
    """
    SPS - Sampling Parameters for Summary Statistics
    
    Description:
        To define the sampling parameters associated with summary statistics
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SPS/
    """
    _id: Literal["SPS"] = id_element(name="SPS")

    Count: Optional[X12Nn] = element(
        name="SPS01",
        description="Count",
        min_length=1,
        max_length=9,
    )

    Count2: Optional[X12Nn] = element(
        name="SPS02",
        description="Count",
        min_length=1,
        max_length=9,
    )

    Count3: Optional[X12Nn] = element(
        name="SPS03",
        description="Count",
        min_length=1,
        max_length=9,
    )

    ConfidenceLimit: Optional[X12R] = element(
        name="SPS04",
        description="Confidence Limit",
        min_length=1,
        max_length=4,
    )

    SampleFrequencyValuePerUnitOfMeasurementCode: Optional[X12Nn] = element(
        name="SPS06",
        description="Sample Frequency Value per Unit of Measurement Code",
        min_length=1,
        max_length=9,
    )
