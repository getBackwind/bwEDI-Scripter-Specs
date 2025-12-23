# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class SL1(Segment):
    """
    SL1 - Tariff Reference
    
    Description:
        To reference details of the tariff used to arrive at applicable rates or charges for customer-requested service
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SL1/
    """
    _id: Literal["SL1"] = id_element(name="SL1")

    ServiceLevelCode: X12ID = element(
        name="SL101",
        description="Service Level Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    TariffNumber: Optional[X12AN] = element(
        name="SL102",
        description="Tariff Number",
        min_length=1,
        max_length=7,
    )

    CommodityCode: Optional[X12AN] = element(
        name="SL103",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    Scale: Optional[X12AN] = element(
        name="SL104",
        description="Scale",
        min_length=1,
        max_length=10,
    )

    Date: Optional[X12DT] = element(
        name="SL105",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ServiceLevelCode2: Optional[X12ID] = element(
        name="SL106",
        description="Service Level Code",
        min_length=2,
        max_length=2,
    )

    ShipmentMethodOfPayment: Optional[X12ID] = element(
        name="SL107",
        description="Shipment Method of Payment",
    )

    DataSourceCode: Optional[X12ID] = element(
        name="SL108",
        description="Data Source Code",
        min_length=2,
        max_length=2,
    )

    InternationalDomesticCode: Optional[X12ID] = element(
        name="SL109",
        description="International/Domestic Code",
        min_length=1,
        max_length=1,
    )
