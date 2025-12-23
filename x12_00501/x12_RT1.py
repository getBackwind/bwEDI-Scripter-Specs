# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class RT1(Segment):
    """
    RT1 - Rate Detail
    
    Description:
        To provide rate details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RT1/
    """
    _id: Literal["RT1"] = id_element(name="RT1")

    TransportationMethodTypeCode: X12ID = element(
        name="RT101",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    VehicleTypeCode: X12ID = element(
        name="RT102",
        description="Vehicle Type Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    FreightRate: X12R = element(
        name="RT103",
        description="Freight Rate",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    RoundingRuleCode: Optional[X12ID] = element(
        name="RT104",
        description="Rounding Rule Code",
        min_length=1,
        max_length=1,
    )

    VehicleIdentificationNumberVINPlantCode: Optional[X12ID] = element(
        name="RT105",
        description="Vehicle Identification Number (VIN) Plant Code",
        min_length=1,
        max_length=1,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="RT106",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    TariffItemNumber: Optional[X12AN] = element(
        name="RT107",
        description="Tariff Item Number",
        min_length=1,
        max_length=16,
    )

    SpecialRateCode: Optional[X12ID] = element(
        name="RT108",
        description="Special Rate Code",
        min_length=2,
        max_length=2,
    )
