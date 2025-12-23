# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class PSD(Segment):
    """
    PSD - Physical Sample Description
    
    Description:
        To define the physical sample parameters associated with a test resulting in discrete measurements
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/PSD/
    """
    _id: Literal["PSD"] = id_element(name="PSD")

    SampleProcessStatusCode: Optional[X12ID] = element(
        name="PSD01",
        description="Sample Process Status Code",
        min_length=2,
        max_length=2,
    )

    SampleSelectionMethodCode: Optional[X12ID] = element(
        name="PSD02",
        description="Sample Selection Method Code",
        min_length=2,
        max_length=2,
    )

    SampleFrequencyValuePerUnitOfMeasurementCode: Optional[X12Nn] = element(
        name="PSD03",
        description="Sample Frequency Value per Unit of Measurement Code",
        min_length=1,
        max_length=9,
    )

    SampleDescriptionCode: Optional[X12ID] = element(
        name="PSD05",
        description="Sample Description Code",
        min_length=2,
        max_length=2,
    )

    SampleDirectionCode: Optional[X12ID] = element(
        name="PSD06",
        description="Sample Direction Code",
        min_length=2,
        max_length=2,
    )

    PositionCode: Optional[X12ID] = element(
        name="PSD07",
        description="Position Code",
        min_length=2,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="PSD08",
        description="Description",
        min_length=1,
        max_length=80,
    )

    SampleSelectionModulus: Optional[X12R] = element(
        name="PSD09",
        description="Sample Selection Modulus",
        min_length=1,
        max_length=6,
    )
