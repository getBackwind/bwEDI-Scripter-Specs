# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class N8(Segment):
    """
    N8 - Waybill Reference
    
    Description:
        To identify the waybill and to specify the equipment used and the destination details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N8/
    """
    _id: Literal["N8"] = id_element(name="N8")

    WaybillNumber: X12Nn = element(
        name="N801",
        description="Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    Date: X12DT = element(
        name="N802",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    CrossReferenceTypeCode: Optional[X12ID] = element(
        name="N803",
        description="Cross Reference Type Code",
        min_length=1,
        max_length=1,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="N804",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="N805",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )

    WaybillNumber2: Optional[X12Nn] = element(
        name="N806",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    Date2: Optional[X12DT] = element(
        name="N807",
        description="Date",
        min_length=8,
        max_length=8,
    )

    CityName: Optional[X12AN] = element(
        name="N808",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="N809",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="N810",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    FreightStationAccountingCode: Optional[X12ID] = element(
        name="N811",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )
