# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class TOA(Segment):
    """
    TOA - Type of Activity
    
    Description:
        To specify type of activity information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TOA/
    """
    _id: Literal["TOA"] = id_element(name="TOA")

    TypeOfActivityCode: X12ID = element(
        name="TOA01",
        description="Type of Activity Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    LicenseTypeCode: Optional[X12ID] = element(
        name="TOA02",
        description="License Type Code",
        min_length=2,
        max_length=2,
    )

    StatusCode: Optional[X12ID] = element(
        name="TOA03",
        description="Status Code",
        min_length=2,
        max_length=2,
    )

    TypeOfRatingCode: Optional[X12ID] = element(
        name="TOA04",
        description="Type of Rating Code",
        min_length=2,
        max_length=2,
    )

    TypeOfRatingCode2: Optional[X12ID] = element(
        name="TOA05",
        description="Type of Rating Code",
        min_length=2,
        max_length=2,
    )
