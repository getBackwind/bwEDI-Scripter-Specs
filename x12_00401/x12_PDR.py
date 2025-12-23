# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class PDR(Segment):
    """
    PDR - Property Description - Real
    
    Description:
        To provide a description of real property
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/PDR/
    """
    _id: Literal["PDR"] = id_element(name="PDR")

    TypeOfRealEstateAssetCode: X12ID = element(
        name="PDR01",
        description="Type of Real Estate Asset Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="PDR02",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="PDR03",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    OccupancyCode: Optional[X12ID] = element(
        name="PDR04",
        description="Occupancy Code",
        min_length=2,
        max_length=2,
    )
