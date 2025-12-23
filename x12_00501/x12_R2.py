# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class R2(Segment):
    """
    R2 - Route Information
    
    Description:
        To specify carrier and routing sequences and details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R2/
    """
    _id: Literal["R2"] = id_element(name="R2")

    StandardCarrierAlphaCode: X12ID = element(
        name="R201",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    RoutingSequenceCode: X12ID = element(
        name="R202",
        description="Routing Sequence Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="R203",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="R204",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    IntermodalServiceCode: Optional[X12ID] = element(
        name="R205",
        description="Intermodal Service Code",
        min_length=1,
        max_length=2,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="R206",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    IntermediateSwitchCarrier: Optional[X12ID] = element(
        name="R207",
        description="Intermediate Switch Carrier",
        min_length=2,
        max_length=4,
    )

    IntermediateSwitchCarrier2: Optional[X12ID] = element(
        name="R208",
        description="Intermediate Switch Carrier",
        min_length=2,
        max_length=4,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="R209",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    Date: Optional[X12DT] = element(
        name="R210",
        description="Date",
        min_length=8,
        max_length=8,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="R211",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="R212",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )

    RouteDescription: Optional[X12AN] = element(
        name="R213",
        description="Route Description",
        min_length=1,
        max_length=35,
    )
