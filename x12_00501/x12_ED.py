# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class ED(Segment):
    """
    ED - Equipment Description
    
    Description:
        To identify further the referenced equipment
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ED/
    """
    _id: Literal["ED"] = id_element(name="ED")

    EquipmentInitial: X12AN = element(
        name="ED01",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="ED02",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    LoadEmptyStatusCode: Optional[X12ID] = element(
        name="ED03",
        description="Load/Empty Status Code",
        min_length=1,
        max_length=1,
    )

    CommodityCode: Optional[X12AN] = element(
        name="ED04",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    LadingDescription: Optional[X12AN] = element(
        name="ED05",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )

    WaybillNumber: Optional[X12Nn] = element(
        name="ED06",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    EquipmentNumber2: Optional[X12AN] = element(
        name="ED07",
        description="Equipment Number",
        min_length=1,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="ED08",
        description="Date",
        min_length=8,
        max_length=8,
    )
