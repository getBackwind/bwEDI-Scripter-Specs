# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class IC(Segment):
    """
    IC - Intermodal Chassis Equipment
    
    Description:
        To specify the chassis equipment details in terms of identifying numbers, weights, and ownership
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IC/
    """
    _id: Literal["IC"] = id_element(name="IC")

    EquipmentInitial: X12AN = element(
        name="IC01",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="IC02",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    TareWeight: Optional[X12Nn] = element(
        name="IC03",
        description="Tare Weight",
        min_length=3,
        max_length=8,
    )

    TareQualifierCode: Optional[X12ID] = element(
        name="IC04",
        description="Tare Qualifier Code",
        min_length=1,
        max_length=1,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="IC05",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    EquipmentLength: Optional[X12Nn] = element(
        name="IC06",
        description="Equipment Length",
        min_length=4,
        max_length=5,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="IC07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    ChassisType: Optional[X12ID] = element(
        name="IC08",
        description="Chassis Type",
    )
