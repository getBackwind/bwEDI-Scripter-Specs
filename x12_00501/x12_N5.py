# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class N5(Segment):
    """
    N5 - Equipment Ordered
    
    Description:
        To specify carrier equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/N5/
    """
    _id: Literal["N5"] = id_element(name="N5")

    EquipmentLength: Optional[X12Nn] = element(
        name="N501",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    WeightCapacity: Optional[X12Nn] = element(
        name="N502",
        description="Weight Capacity",
        min_length=2,
        max_length=3,
    )

    CubicCapacity: Optional[X12Nn] = element(
        name="N503",
        description="Cubic Capacity",
        min_length=2,
        max_length=5,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="N504",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    MetricQualifier: Optional[X12ID] = element(
        name="N505",
        description="Metric Qualifier",
        min_length=1,
        max_length=1,
    )

    Height: Optional[X12R] = element(
        name="N506",
        description="Height",
        min_length=1,
        max_length=8,
    )

    LadingPercentage: Optional[X12Nn] = element(
        name="N507",
        description="Lading Percentage",
        min_length=2,
        max_length=4,
    )

    LadingPercentQualifier: Optional[X12ID] = element(
        name="N508",
        description="Lading Percent Qualifier",
        min_length=1,
        max_length=1,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="N509",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )
