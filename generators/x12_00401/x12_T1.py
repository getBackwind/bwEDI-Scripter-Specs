# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class T1(Segment):
    """
    T1 - Transit Inbound Origin
    
    Description:
        To specify origin point and waybill references of movement to transit waybill point
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/T1/
    """
    _id: Literal["T1"] = id_element(name="T1")

    AssignedNumber: X12Nn = element(
        name="T101",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    WaybillNumber: Optional[X12Nn] = element(
        name="T102",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    Date: Optional[X12DT] = element(
        name="T103",
        description="Date",
        min_length=8,
        max_length=8,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="T104",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    CityName: Optional[X12AN] = element(
        name="T105",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="T106",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="T107",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    TransitRegistrationNumber: Optional[X12AN] = element(
        name="T108",
        description="Transit Registration Number",
        min_length=1,
        max_length=6,
    )

    TransitLevelCode: Optional[X12ID] = element(
        name="T109",
        description="Transit Level Code",
        min_length=1,
        max_length=3,
    )
