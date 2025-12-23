# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class SCO(Segment):
    """
    SCO - Shipper's Car Ordered
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SCO/
    """
    _id: Literal["SCO"] = id_element(name="SCO")

    Quantity: X12R = element(
        name="SCO01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    CommodityCodeQualifier: X12ID = element(
        name="SCO02",
        description="Commodity Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    CommodityCode: X12AN = element(
        name="SCO03",
        description="Commodity Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="SCO04",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="SCO05",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="SCO06",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    EquipmentLength: Optional[X12Nn] = element(
        name="SCO07",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    Height: Optional[X12R] = element(
        name="SCO08",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="SCO09",
        description="Width",
        min_length=1,
        max_length=8,
    )

    WeightCapacity: Optional[X12Nn] = element(
        name="SCO10",
        description="Weight Capacity",
        min_length=2,
        max_length=3,
    )

    CubicCapacity: Optional[X12Nn] = element(
        name="SCO11",
        description="Cubic Capacity",
        min_length=2,
        max_length=4,
    )

    ProtectiveServiceCode: Optional[X12ID] = element(
        name="SCO12",
        description="Protective Service Code",
        min_length=1,
        max_length=3,
    )

    Temperature: Optional[X12R] = element(
        name="SCO13",
        description="Temperature",
        min_length=1,
        max_length=4,
    )

    FloorTypeCode: Optional[X12ID] = element(
        name="SCO14",
        description="Floor Type Code",
        min_length=1,
        max_length=1,
    )

    Height2: Optional[X12R] = element(
        name="SCO15",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width2: Optional[X12R] = element(
        name="SCO16",
        description="Width",
        min_length=1,
        max_length=8,
    )

    DoorTypeCode: Optional[X12ID] = element(
        name="SCO17",
        description="Door Type Code",
        min_length=2,
        max_length=2,
    )

    CarTypeCode2: Optional[X12ID] = element(
        name="SCO18",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )
