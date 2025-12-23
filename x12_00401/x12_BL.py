# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BL(Segment):
    """
    BL - Billing Information
    
    Description:
        To identify the individual billing segments within a movement when joint rail rates have been established between carriers but do not cover the entire movement
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BL/
    """
    _id: Literal["BL"] = id_element(name="BL")

    RebillReasonCode: X12ID = element(
        name="BL01",
        description="Rebill Reason Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    FreightStationAccountingCode: X12ID = element(
        name="BL02",
        description="Freight Station Accounting Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    FreightStationAccountingCode2: X12ID = element(
        name="BL03",
        description="Freight Station Accounting Code",
        mandatory=True,
        min_length=1,
        max_length=5,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="BL04",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    CityName: Optional[X12AN] = element(
        name="BL05",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="BL06",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode: Optional[X12ID] = element(
        name="BL07",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="BL08",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    CityName2: Optional[X12AN] = element(
        name="BL09",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode2: Optional[X12ID] = element(
        name="BL10",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CountryCode2: Optional[X12ID] = element(
        name="BL11",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="BL12",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="BL13",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="BL14",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode4: Optional[X12ID] = element(
        name="BL15",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode5: Optional[X12ID] = element(
        name="BL16",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    StandardCarrierAlphaCode6: Optional[X12ID] = element(
        name="BL17",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
