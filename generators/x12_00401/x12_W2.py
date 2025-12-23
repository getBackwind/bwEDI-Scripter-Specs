# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class W2(Segment):
    """
    W2 - Equipment Identification
    
    Description:
        To identify equipment and the commodity being carried
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/W2/
    """
    _id: Literal["W2"] = id_element(name="W2")

    EquipmentInitial: X12AN = element(
        name="W201",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="W202",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    CommodityCode: Optional[X12AN] = element(
        name="W203",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    EquipmentDescriptionCode: X12ID = element(
        name="W204",
        description="Equipment Description Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    EquipmentStatusCode: X12ID = element(
        name="W205",
        description="Equipment Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    NetTons: Optional[X12Nn] = element(
        name="W206",
        description="Net Tons",
        min_length=1,
        max_length=3,
    )

    IntermodalServiceCode: Optional[X12ID] = element(
        name="W207",
        description="Intermodal Service Code",
        min_length=1,
        max_length=2,
    )

    CarServiceOrderCode: Optional[X12ID] = element(
        name="W208",
        description="Car Service Order Code",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="W209",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TypeOfLocomotiveMaintenanceCode: Optional[X12AN] = element(
        name="W210",
        description="Type of Locomotive Maintenance Code",
        min_length=2,
        max_length=2,
    )

    EquipmentInitial2: Optional[X12AN] = element(
        name="W211",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber2: Optional[X12AN] = element(
        name="W212",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    EquipmentNumberCheckDigit: Optional[X12Nn] = element(
        name="W213",
        description="Equipment Number Check Digit",
        min_length=1,
        max_length=1,
    )

    Position: Optional[X12AN] = element(
        name="W214",
        description="Position",
        min_length=1,
        max_length=3,
    )

    CarTypeCode: Optional[X12ID] = element(
        name="W215",
        description="Car Type Code",
        min_length=1,
        max_length=4,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="W216",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
