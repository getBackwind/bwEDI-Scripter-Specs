# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class N7(Segment):
    """
    N7 - Equipment Details
    
    Description:
        To identify the equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/N7/
    """
    _id: Literal["N7"] = id_element(name="N7")

    EquipmentInitial: Optional[X12AN] = element(
        name="N701",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="N702",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    Weight: Optional[X12R] = element(
        name="N703",
        description="Weight",
        min_length=1,
        max_length=10,
    )

    WeightQualifier: Optional[X12ID] = element(
        name="N704",
        description="Weight Qualifier",
        min_length=1,
        max_length=2,
    )

    TareWeight: Optional[X12Nn] = element(
        name="N705",
        description="Tare Weight",
        min_length=3,
        max_length=8,
    )

    WeightAllowance: Optional[X12Nn] = element(
        name="N706",
        description="Weight Allowance",
        min_length=2,
        max_length=6,
    )

    Dunnage: Optional[X12Nn] = element(
        name="N707",
        description="Dunnage",
        min_length=1,
        max_length=6,
    )

    Volume: Optional[X12R] = element(
        name="N708",
        description="Volume",
        min_length=1,
        max_length=8,
    )

    VolumeUnitQualifier: Optional[X12ID] = element(
        name="N709",
        description="Volume Unit Qualifier",
        min_length=1,
        max_length=1,
    )

    OwnershipCode: Optional[X12ID] = element(
        name="N710",
        description="Ownership Code",
        min_length=1,
        max_length=1,
    )

    EquipmentDescriptionCode: Optional[X12ID] = element(
        name="N711",
        description="Equipment Description Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="N712",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    TemperatureControl: Optional[X12AN] = element(
        name="N713",
        description="Temperature Control",
        min_length=3,
        max_length=6,
    )

    Position: Optional[X12AN] = element(
        name="N714",
        description="Position",
        min_length=1,
        max_length=3,
    )

    EquipmentLength: Optional[X12Nn] = element(
        name="N715",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    TareQualifierCode: Optional[X12ID] = element(
        name="N716",
        description="Tare Qualifier Code",
        min_length=1,
        max_length=1,
    )

    WeightUnitCode: Optional[X12ID] = element(
        name="N717",
        description="Weight Unit Code",
        min_length=1,
        max_length=1,
    )

    EquipmentNumberCheckDigit: Optional[X12Nn] = element(
        name="N718",
        description="Equipment Number Check Digit",
        min_length=1,
        max_length=1,
    )

    TypeOfServiceCode: Optional[X12ID] = element(
        name="N719",
        description="Type of Service Code",
        min_length=2,
        max_length=2,
    )

    Height: Optional[X12R] = element(
        name="N720",
        description="Height",
        min_length=1,
        max_length=8,
    )

    Width: Optional[X12R] = element(
        name="N721",
        description="Width",
        min_length=1,
        max_length=8,
    )

    EquipmentType: Optional[X12ID] = element(
        name="N722",
        description="Equipment Type",
        min_length=4,
        max_length=4,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="N723",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="N724",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )
