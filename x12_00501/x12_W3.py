# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class W3(Segment):
    """
    W3 - Consignee Information
    
    Description:
        To provide sufficient waybill information for delivery of shipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W3/
    """
    _id: Literal["W3"] = id_element(name="W3")

    WaybillNumber: Optional[X12Nn] = element(
        name="W301",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    Date: Optional[X12DT] = element(
        name="W302",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AbbreviatedCustomerName: Optional[X12AN] = element(
        name="W303",
        description="Abbreviated Customer Name",
        min_length=2,
        max_length=12,
    )

    CityName: Optional[X12AN] = element(
        name="W304",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="W305",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    CityNameQualifierCode: Optional[X12ID] = element(
        name="W306",
        description="City Name Qualifier Code",
        min_length=1,
        max_length=1,
    )
