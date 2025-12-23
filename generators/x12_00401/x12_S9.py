# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class S9(Segment):
    """
    S9 - Stop-off Station
    
    Description:
        To specify location details for a stop-off
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/S9/
    """
    _id: Literal["S9"] = id_element(name="S9")

    StopSequenceNumber: X12Nn = element(
        name="S901",
        description="Stop Sequence Number",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="S902",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    CityName: X12AN = element(
        name="S903",
        description="City Name",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: X12ID = element(
        name="S904",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="S905",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    StopReasonCode: X12ID = element(
        name="S906",
        description="Stop Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="S907",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="S908",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )
