# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SMR(Segment):
    """
    SMR - Cross Reference
    
    Description:
        To identify the specific station that indicates the switching district for a given railroad terminal or the specific station used to identify a geographical location as a rate base location
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SMR/
    """
    _id: Literal["SMR"] = id_element(name="SMR")

    LocationQualifier: X12ID = element(
        name="SMR01",
        description="Location Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="SMR02",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    CityName: Optional[X12AN] = element(
        name="SMR03",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="SMR04",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
