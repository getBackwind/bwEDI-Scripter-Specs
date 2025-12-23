# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class F9(Segment):
    """
    F9 - Origin Station
    
    Description:
        To identify the rail origin of the shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/F9/
    """
    _id: Literal["F9"] = id_element(name="F9")

    FreightStationAccountingCode: Optional[X12ID] = element(
        name="F901",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )

    CityName: X12AN = element(
        name="F902",
        description="City Name",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: X12ID = element(
        name="F903",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="F904",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    FreightStationAccountingCode2: Optional[X12ID] = element(
        name="F905",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )

    CityName2: Optional[X12AN] = element(
        name="F906",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="F907",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="F908",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    PostalCode: Optional[X12ID] = element(
        name="F909",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="F910",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    PostalCode2: Optional[X12ID] = element(
        name="F911",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    CountryCode2: Optional[X12ID] = element(
        name="F912",
        description="Country Code",
        min_length=2,
        max_length=3,
    )
