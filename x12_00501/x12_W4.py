# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class W4(Segment):
    """
    W4 - Consignor Information
    
    Description:
        To provide sufficient information to identify the origin of shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W4/
    """
    _id: Literal["W4"] = id_element(name="W4")

    AbbreviatedCustomerName: Optional[X12AN] = element(
        name="W401",
        description="Abbreviated Customer Name",
        min_length=2,
        max_length=12,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="W402",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    FreightStationAccountingCode: Optional[X12ID] = element(
        name="W403",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )

    CityName: Optional[X12AN] = element(
        name="W404",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="W405",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
