# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class R9(Segment):
    """
    R9 - Route Code Identification
    
    Description:
        To specify the route using a single code
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R9/
    """
    _id: Literal["R9"] = id_element(name="R9")

    RouteCode: X12AN = element(
        name="R901",
        description="Route Code",
        mandatory=True,
        min_length=1,
        max_length=13,
    )

    AgentShipperRoutingCode: Optional[X12ID] = element(
        name="R902",
        description="Agent/Shipper Routing Code",
        min_length=1,
        max_length=1,
    )

    IntermodalServiceCode: Optional[X12ID] = element(
        name="R903",
        description="Intermodal Service Code",
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="R904",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ActionCode: Optional[X12ID] = element(
        name="R905",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="R906",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="R907",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="R908",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    RouteCode2: Optional[X12AN] = element(
        name="R909",
        description="Route Code",
        min_length=1,
        max_length=13,
    )
