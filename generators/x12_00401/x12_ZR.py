# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class ZR(Segment):
    """
    ZR - Waybill Reference Identification
    
    Description:
        To transmit identity and reference information of the waybill
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ZR/
    """
    _id: Literal["ZR"] = id_element(name="ZR")

    WaybillResponseCode: X12ID = element(
        name="ZR01",
        description="Waybill Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    EquipmentInitial: X12AN = element(
        name="ZR02",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="ZR03",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=10,
    )

    WaybillNumber: Optional[X12Nn] = element(
        name="ZR04",
        description="Waybill Number",
        min_length=1,
        max_length=6,
    )

    Date: Optional[X12DT] = element(
        name="ZR05",
        description="Date",
        min_length=8,
        max_length=8,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="ZR06",
        description="Free Form Message",
        min_length=1,
        max_length=60,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="ZR07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    Date2: Optional[X12DT] = element(
        name="ZR08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    InterlineSettlementSystemStatusActionOrDisputeCode: Optional[X12ID] = element(
        name="ZR09",
        description="Interline Settlement System Status Action or Dispute Code",
        min_length=2,
        max_length=2,
    )

    InterlineSettlementSystemStatusActionOrDisputeCode2: Optional[X12ID] = element(
        name="ZR10",
        description="Interline Settlement System Status Action or Dispute Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="ZR11",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="ZR12",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    CorrectionIndicator: Optional[X12ID] = element(
        name="ZR13",
        description="Correction Indicator",
    )
