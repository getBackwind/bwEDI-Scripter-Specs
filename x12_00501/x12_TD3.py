# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class TD3(Segment):
    """
    TD3 - Carrier Details (Equipment)
    
    Description:
        To specify transportation details relating to the equipment used by the carrier
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/TD3/
    """
    _id: Literal["TD3"] = id_element(name="TD3")

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="TD301",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="TD302",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="TD303",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="TD304",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    Weight: Optional[X12R] = element(
        name="TD305",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    UnitOrBasisForMeasurementCode: Optional[X12ID] = element(
        name="TD306",
        description="Unit or Basis for Measurement Code",
        min_length=2,
        max_length=2,
    )

    OwnershipCode: Optional[X12ID] = element(
        name="TD307",
        description="Ownership Code",
        min_length=1,
        max_length=1,
    )

    SealStatusCode: Optional[X12ID] = element(
        name="TD308",
        description="Seal Status Code",
        min_length=2,
        max_length=2,
    )

    SealNumber: Optional[X12AN] = element(
        name="TD309",
        description="Seal Number",
        min_length=2,
        max_length=15,
    )

    EquipmentType: Optional[X12ID] = element(
        name="TD310",
        description="Equipment Type",
        min_length=4,
        max_length=4,
    )
