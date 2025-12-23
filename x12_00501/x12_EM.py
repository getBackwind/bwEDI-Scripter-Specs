# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class EM(Segment):
    """
    EM - Equipment Characteristics
    
    Description:
        To send additional information regarding a specific piece of equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EM/
    """
    _id: Literal["EM"] = id_element(name="EM")

    WeightUnitCode: Optional[X12ID] = element(
        name="EM01",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    Weight: Optional[X12R] = element(
        name="EM02",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="EM03",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    Volume: Optional[X12R] = element(
        name="EM04",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    CountryCode: Optional[X12ID] = element(
        name="EM05",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    ConstructionType: Optional[X12ID] = element(
        name="EM06",
        description="Construction Type",
    )

    Date: Optional[X12DT] = element(
        name="EM07",
        description="Date",
        min_length=8,
        max_length=8,
    )
