# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class H5(Segment):
    """
    H5 - Car Service Order
    
    Description:
        To identify the car service directive or other car movement instructions applicable to the empty movement of the car
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/H5/
    """
    _id: Literal["H5"] = id_element(name="H5")

    CarServiceOrderCode: X12ID = element(
        name="H501",
        description="Car Service Order Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    CityName: Optional[X12AN] = element(
        name="H502",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="H503",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
