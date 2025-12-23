# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SMA(Segment):
    """
    SMA - Station Address
    
    Description:
        To identify the specific postal address information for each of the various categories of mailing requirements for a station
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SMA/
    """
    _id: Literal["SMA"] = id_element(name="SMA")

    AddressTypeCode: X12ID = element(
        name="SMA01",
        description="Address Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    AddressInformation: X12AN = element(
        name="SMA02",
        description="Address Information",
        mandatory=True,
        min_length=1,
        max_length=55,
    )

    CityName: X12AN = element(
        name="SMA03",
        description="City Name",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: X12ID = element(
        name="SMA04",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    PostalCode: X12ID = element(
        name="SMA05",
        description="Postal Code",
        mandatory=True,
        min_length=3,
        max_length=15,
    )
