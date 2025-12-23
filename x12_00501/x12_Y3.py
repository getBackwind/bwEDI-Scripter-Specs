# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class Y3(Segment):
    """
    Y3 - Space Confirmation
    
    Description:
        To specify confirmation information for space booking including numbers, dates, and load time
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/Y3/
    """
    _id: Literal["Y3"] = id_element(name="Y3")

    BookingNumber: X12AN = element(
        name="Y301",
        description="Booking Number",
        mandatory=True,
        min_length=1,
        max_length=17,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="Y302",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Date: Optional[X12DT] = element(
        name="Y303",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="Y304",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="Y305",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    PierName: Optional[X12AN] = element(
        name="Y306",
        description="Pier Name",
        min_length=2,
        max_length=14,
    )

    Date3: Optional[X12DT] = element(
        name="Y307",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="Y308",
        description="Time",
        min_length=4,
        max_length=8,
    )

    TransportationMethodTypeCode: Optional[X12ID] = element(
        name="Y309",
        description="Transportation Method/Type Code",
        min_length=1,
        max_length=2,
    )

    TariffServiceCode: Optional[X12ID] = element(
        name="Y310",
        description="Tariff Service Code",
        min_length=2,
        max_length=2,
    )

    TimeCode: Optional[X12ID] = element(
        name="Y311",
        description="Time Code",
        min_length=2,
        max_length=2,
    )
