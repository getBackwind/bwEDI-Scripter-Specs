# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class R1(Segment):
    """
    R1 - Route Information (Air)
    
    Description:
        To specify airline and airport routing sequences
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/R1/
    """
    _id: Literal["R1"] = id_element(name="R1")

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="R101",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="R102",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    AirportCode: X12ID = element(
        name="R103",
        description="Airport Code",
        mandatory=True,
        min_length=3,
        max_length=5,
    )

    AirCarrierCode: X12ID = element(
        name="R104",
        description="Air Carrier Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    AirportCode2: X12ID = element(
        name="R105",
        description="Airport Code",
        mandatory=True,
        min_length=3,
        max_length=5,
    )

    AirCarrierCode2: Optional[X12ID] = element(
        name="R106",
        description="Air Carrier Code",
        min_length=3,
        max_length=3,
    )

    AirportCode3: Optional[X12ID] = element(
        name="R107",
        description="Airport Code",
        min_length=3,
        max_length=5,
    )

    AirCarrierCode3: Optional[X12ID] = element(
        name="R108",
        description="Air Carrier Code",
        min_length=3,
        max_length=3,
    )

    AirportCode4: Optional[X12ID] = element(
        name="R109",
        description="Airport Code",
        min_length=3,
        max_length=5,
    )

    AirCarrierCode4: Optional[X12ID] = element(
        name="R110",
        description="Air Carrier Code",
        min_length=3,
        max_length=3,
    )

    AirportCode5: Optional[X12ID] = element(
        name="R111",
        description="Airport Code",
        min_length=3,
        max_length=5,
    )

    AirCarrierCode5: Optional[X12ID] = element(
        name="R112",
        description="Air Carrier Code",
        min_length=3,
        max_length=3,
    )

    AirportCode6: Optional[X12ID] = element(
        name="R113",
        description="Airport Code",
        min_length=3,
        max_length=5,
    )
