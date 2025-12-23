# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn, X12R, X12TM


class V9(Segment):
    """
    V9 - Event Detail
    
    Description:
        To specify information about a specific event
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/V9/
    """
    _id: Literal["V9"] = id_element(name="V9")

    EventCode: X12ID = element(
        name="V901",
        description="Event Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    Event: Optional[X12AN] = element(
        name="V902",
        description="Event",
        min_length=1,
        max_length=25,
    )

    Date: Optional[X12DT] = element(
        name="V903",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="V904",
        description="Time",
        min_length=4,
        max_length=8,
    )

    CityName: Optional[X12AN] = element(
        name="V905",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="V906",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="V907",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="V908",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="V909",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    Quantity: Optional[X12R] = element(
        name="V910",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    TrainDelayReasonCode: Optional[X12AN] = element(
        name="V911",
        description="Train Delay Reason Code",
        min_length=2,
        max_length=3,
    )

    FreeFormInformation: Optional[X12AN] = element(
        name="V912",
        description="Free-form Information",
        min_length=1,
        max_length=30,
    )

    TimeCode: Optional[X12ID] = element(
        name="V913",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    Quantity2: Optional[X12R] = element(
        name="V914",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="V915",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    TotalEquipment: Optional[X12Nn] = element(
        name="V916",
        description="Total Equipment",
        min_length=1,
        max_length=3,
    )

    TotalEquipment2: Optional[X12Nn] = element(
        name="V917",
        description="Total Equipment",
        min_length=1,
        max_length=3,
    )

    TotalEquipment3: Optional[X12Nn] = element(
        name="V918",
        description="Total Equipment",
        min_length=1,
        max_length=3,
    )

    Weight: Optional[X12R] = element(
        name="V919",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    Length: Optional[X12R] = element(
        name="V920",
        description="Length",
        min_length=1,
        max_length=8,
    )
