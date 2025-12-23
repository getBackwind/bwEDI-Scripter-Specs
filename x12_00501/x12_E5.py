# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class E5(Segment):
    """
    E5 - Empty Car Disposition - Pended Destination Route
    
    Description:
        To specify the routing of the empty car
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E5/
    """
    _id: Literal["E5"] = id_element(name="E5")

    StandardCarrierAlphaCode: X12ID = element(
        name="E501",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    RoutingSequenceCode: X12ID = element(
        name="E502",
        description="Routing Sequence Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="E503",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="E504",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )
