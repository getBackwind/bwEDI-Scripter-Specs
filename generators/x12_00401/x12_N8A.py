# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class N8A(Segment):
    """
    N8A - Additional Reference Information
    
    Description:
        To identify additional station and waybill or station, or waybill information pertaining to revenue waybill
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/N8A/
    """
    _id: Literal["N8A"] = id_element(name="N8A")

    WaybillCrossReferenceCode: Optional[X12ID] = element(
        name="N8A01",
        description="Waybill Cross-Reference Code",
        min_length=2,
        max_length=2,
    )

    WaybillNumber: Optional[X12Nn] = element(
        name="N8A02",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    Date: Optional[X12DT] = element(
        name="N8A03",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="N8A04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    CityName: Optional[X12AN] = element(
        name="N8A05",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="N8A06",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="N8A07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    FreightStationAccountingCode: Optional[X12ID] = element(
        name="N8A08",
        description="Freight Station Accounting Code",
        min_length=1,
        max_length=5,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="N8A09",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: Optional[X12AN] = element(
        name="N8A10",
        description="Equipment Number",
        min_length=1,
        max_length=10,
    )
