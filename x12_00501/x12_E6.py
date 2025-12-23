# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class E6(Segment):
    """
    E6 - Advance Car Disposition
    
    Description:
        To specify advance data on the disposition of equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/E6/
    """
    _id: Literal["E6"] = id_element(name="E6")

    EquipmentInitial: X12AN = element(
        name="E601",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="E602",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    CityName: X12AN = element(
        name="E603",
        description="City Name",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    StandardPointLocationCode: Optional[X12ID] = element(
        name="E604",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="E605",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    IntermediateSwitchCarrier: Optional[X12ID] = element(
        name="E606",
        description="Intermediate Switch Carrier",
        min_length=2,
        max_length=4,
    )

    CommodityCode: Optional[X12AN] = element(
        name="E607",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="E608",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    EquipmentStatusCode: X12ID = element(
        name="E609",
        description="Equipment Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )
