# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class SCR(Segment):
    """
    SCR - Shipper's Car Ordered Rail
    
    Description:
        To be Monitored
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SCR/
    """
    _id: Literal["SCR"] = id_element(name="SCR")

    Quantity: Optional[X12R] = element(
        name="SCR01",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    CommodityCode: Optional[X12AN] = element(
        name="SCR02",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="SCR03",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    EquipmentLength: Optional[X12Nn] = element(
        name="SCR04",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    Height: Optional[X12R] = element(
        name="SCR05",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="SCR06",
        description="Width",
        min_length=1,
        max_length=8,
    )

    WeightCapacity: Optional[X12Nn] = element(
        name="SCR07",
        description="Weight Capacity",
        min_length=2,
        max_length=3,
    )

    CubicCapacity: Optional[X12Nn] = element(
        name="SCR08",
        description="Cubic Capacity",
        min_length=2,
        max_length=5,
    )

    ProtectiveServiceRuleCode: Optional[X12ID] = element(
        name="SCR09",
        description="Protective Service Rule Code",
        min_length=3,
        max_length=9,
    )

    Temperature: Optional[X12R] = element(
        name="SCR10",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    FloorTypeCode: Optional[X12ID] = element(
        name="SCR11",
        description="Floor Type Code",
        min_length=1,
        max_length=1,
    )

    Height2: Optional[X12R] = element(
        name="SCR12",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width2: Optional[X12R] = element(
        name="SCR13",
        description="Width",
        min_length=1,
        max_length=8,
    )

    DoorTypeCode: Optional[X12ID] = element(
        name="SCR14",
        description="Door Type Code",
        min_length=2,
        max_length=2,
    )

    RatingSummaryValueCode: Optional[X12ID] = element(
        name="SCR15",
        description="Rating Summary Value Code",
        min_length=1,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="SCR16",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="SCR17",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    CarTypeCode2: Optional[X12ID] = element(
        name="SCR18",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    AssociationOfAmericanRailroadsAARPoolCode: Optional[X12ID] = element(
        name="SCR19",
        description="Association of American Railroads (AAR) Pool Code",
        min_length=7,
        max_length=7,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="SCR20",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="SCR21",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="SCR22",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="SCR23",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    EquipmentNumber2: Optional[X12AN] = element(
        name="SCR24",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )
