# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class SMS(Segment):
    """
    SMS - Station Codes Segment
    
    Description:
        To identify the specific railroad carrier codes associated with the station
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SMS/
    """
    _id: Literal["SMS"] = id_element(name="SMS")

    StandardCarrierAlphaCode: X12ID = element(
        name="SMS01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    FreightStationAccountingCode: X12ID = element(
        name="SMS02",
        description="Freight Station Accounting Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    Rule260JunctionCode: Optional[X12ID] = element(
        name="SMS03",
        description="Rule 260 Junction Code",
        min_length=1,
        max_length=5,
    )

    PostalCode: Optional[X12ID] = element(
        name="SMS04",
        description="Postal Code",
        min_length=3,
        max_length=15,
    )

    ReciprocalSwitchCode: Optional[X12ID] = element(
        name="SMS05",
        description="Reciprocal Switch Code",
        min_length=1,
        max_length=1,
    )

    TimeCode: Optional[X12ID] = element(
        name="SMS06",
        description="Time Code",
        min_length=2,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="SMS07",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="SMS08",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SMS09",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="SMS10",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SMS11",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
