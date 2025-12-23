# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class GR2(Segment):
    """
    GR2 - Train Data
    
    Description:
        To provide train assignment as to its identification and departure
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/GR2/
    """
    _id: Literal["GR2"] = id_element(name="GR2")

    StandardCarrierAlphaCode: X12ID = element(
        name="GR201",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="GR202",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="GR203",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    CityName: Optional[X12AN] = element(
        name="GR204",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="GR205",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="GR206",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="GR207",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )

    Date: Optional[X12DT] = element(
        name="GR208",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="GR209",
        description="Time",
        min_length=4,
        max_length=8,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="GR210",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="GR211",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    InterchangeTrainIdentification2: Optional[X12AN] = element(
        name="GR212",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )
