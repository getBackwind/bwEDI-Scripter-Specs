# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class ZT(Segment):
    """
    ZT - Waybill Request Information
    
    Description:
        To transmit identity and reference information of the waybill being requested
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ZT/
    """
    _id: Literal["ZT"] = id_element(name="ZT")

    WaybillRequestCode: X12ID = element(
        name="ZT01",
        description="Waybill Request Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    EquipmentInitial: X12AN = element(
        name="ZT02",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="ZT03",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    WaybillNumber: Optional[X12Nn] = element(
        name="ZT04",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    Date: Optional[X12DT] = element(
        name="ZT05",
        description="Date",
        min_length=8,
        max_length=8,
    )
