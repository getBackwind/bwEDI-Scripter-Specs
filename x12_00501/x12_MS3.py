# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class MS3(Segment):
    """
    MS3 - Interline Information
    
    Description:
        To identify the interline carrier and relevant data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MS3/
    """
    _id: Literal["MS3"] = id_element(name="MS3")

    StandardCarrierAlphaCode: X12ID = element(
        name="MS301",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    RoutingSequenceCode: X12ID = element(
        name="MS302",
        description="Routing Sequence Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="MS303",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="MS304",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="MS305",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
