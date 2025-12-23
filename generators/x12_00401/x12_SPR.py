# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SPR(Segment):
    """
    SPR - Supplier Rating
    
    Description:
        To convey a rating value or score of a trading partner
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SPR/
    """
    _id: Literal["SPR"] = id_element(name="SPR")

    RatingCategoryCode: Optional[X12ID] = element(
        name="SPR01",
        description="Rating Category Code",
        min_length=2,
        max_length=2,
    )

    MeasurementValue: Optional[X12R] = element(
        name="SPR02",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )

    RangeMinimum: Optional[X12R] = element(
        name="SPR03",
        description="Range Minimum",
        min_length=1,
        max_length=20,
    )

    RangeMaximum: Optional[X12R] = element(
        name="SPR04",
        description="Range Maximum",
        min_length=1,
        max_length=20,
    )

    RatingSummaryValueCode: Optional[X12ID] = element(
        name="SPR05",
        description="Rating Summary Value Code",
        min_length=1,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="SPR06",
        description="Description",
        min_length=1,
        max_length=80,
    )

    MeasurementValue2: Optional[X12R] = element(
        name="SPR07",
        description="Measurement Value",
        min_length=1,
        max_length=20,
    )
