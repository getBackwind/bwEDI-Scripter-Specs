# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class IS2(Segment):
    """
    IS2 - Scheduled Events
    
    Description:
        To transmit scheduled events such as arrivals, departures, and interchange times
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/IS2/
    """
    _id: Literal["IS2"] = id_element(name="IS2")

    StandardCarrierAlphaCode: X12ID = element(
        name="IS201",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    EventCode: X12ID = element(
        name="IS202",
        description="Event Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    AccomplishCode: X12ID = element(
        name="IS203",
        description="Accomplish Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    StandardPointLocationCode: X12ID = element(
        name="IS204",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    Date: X12DT = element(
        name="IS205",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: X12TM = element(
        name="IS206",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    TimeCode: Optional[X12ID] = element(
        name="IS207",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="IS208",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="IS209",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )

    Date2: Optional[X12DT] = element(
        name="IS210",
        description="Date",
        min_length=8,
        max_length=8,
    )

    BlockIdentifier: Optional[X12AN] = element(
        name="IS211",
        description="Block Identifier",
        min_length=1,
        max_length=12,
    )

    Date3: Optional[X12DT] = element(
        name="IS212",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="IS213",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Date4: Optional[X12DT] = element(
        name="IS214",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time3: Optional[X12TM] = element(
        name="IS215",
        description="Time",
        min_length=4,
        max_length=8,
    )

    CityName: Optional[X12AN] = element(
        name="IS216",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="IS217",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
