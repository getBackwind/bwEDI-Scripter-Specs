# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class T3(Segment):
    """
    T3 - Transit Inbound Route
    
    Description:
        To specify transit inbound routing, including equipment identifications for associated T1 and T2 segments
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/T3/
    """
    _id: Literal["T3"] = id_element(name="T3")

    AssignedNumber: X12Nn = element(
        name="T301",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="T302",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    RoutingSequenceCode: Optional[X12ID] = element(
        name="T303",
        description="Routing Sequence Code",
        min_length=1,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="T304",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="T305",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="T306",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="T307",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )
