# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12Nn, X12R


class CSF(Segment):
    """
    CSF - Conditional Sampling Frequency
    
    Description:
        To represent sampling frequency changes or values that are conditional on measurements made on previous samples, related manufacturing stages, or the environment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CSF/
    """
    _id: Literal["CSF"] = id_element(name="CSF")

    SampleSelectionModulus: Optional[X12R] = element(
        name="CSF02",
        description="Sample Selection Modulus",
        min_length=1,
        max_length=6,
    )

    SampleFrequencyValuePerUnitOfMeasurementCode: Optional[X12Nn] = element(
        name="CSF03",
        description="Sample Frequency Value per Unit of Measurement Code",
        min_length=1,
        max_length=9,
    )
