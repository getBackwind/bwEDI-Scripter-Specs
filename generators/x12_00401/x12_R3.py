# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class R3(Segment):
    """
    R3 - Route Information - Motor
    
    Description:
        To specify carrier and routing sequences and details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/R3/
    """
    _id: Literal["R3"] = id_element(name="R3")

    StandardCarrierAlphaCode: X12ID = element(
        name="R301",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    RoutingSequenceCode: X12ID = element(
        name="R302",
        description="Routing Sequence Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    CityName: Optional[X12AN] = element(
        name="R303",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="R304",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="R305",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="R306",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    Date: Optional[X12DT] = element(
        name="R307",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Amount: Optional[X12Nn] = element(
        name="R308",
        description="Amount",
        min_length=1,
        max_length=15,
    )

    FreeFormDescription: Optional[X12AN] = element(
        name="R309",
        description="Free-form Description",
        min_length=1,
        max_length=45,
    )

    ServiceLevelCode: Optional[X12ID] = element(
        name="R310",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    ServiceLevelCode2: Optional[X12ID] = element(
        name="R311",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    ServiceLevelCode3: Optional[X12ID] = element(
        name="R312",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )
