# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class E4(Segment):
    """
    E4 - Empty Car Disposition - Pended Destination City
    
    Description:
        To specify the geographic place of named party receiving the empty car
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/E4/
    """
    _id: Literal["E4"] = id_element(name="E4")

    CityName: X12AN = element(
        name="E401",
        description="City Name",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: X12ID = element(
        name="E402",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    PostalCode: Optional[X12ID] = element(
        name="E403",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    CountryCode: Optional[X12ID] = element(
        name="E404",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
