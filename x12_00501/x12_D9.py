# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class D9(Segment):
    """
    D9 - Destination Station
    
    Description:
        To identify the rail destination of the shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/D9/
    """
    _id: Literal["D9"] = id_element(name="D9")

    FreightStationAccountingCode: Optional[X12ID] = element(
        name="D901",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )

    CityName: X12AN = element(
        name="D902",
        description="City Name",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: X12ID = element(
        name="D903",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="D904",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    FreightStationAccountingCode2: Optional[X12ID] = element(
        name="D905",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )

    CityName2: Optional[X12AN] = element(
        name="D906",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="D907",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="D908",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    PostalCode: Optional[X12ID] = element(
        name="D909",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="D910",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    PostalCode2: Optional[X12ID] = element(
        name="D911",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    CountryCode2: Optional[X12ID] = element(
        name="D912",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
