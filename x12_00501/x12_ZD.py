# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class ZD(Segment):
    """
    ZD - Transaction Set Deletion - ID, Reason, and Source
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ZD/
    """
    _id: Literal["ZD"] = id_element(name="ZD")

    TransactionSetIdentifierCode: X12ID = element(
        name="ZD01",
        description="Transaction Set Identifier Code",
        mandatory=True,
        min_length=3,
        max_length=3,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="ZD02",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    EquipmentInitial: X12AN = element(
        name="ZD03",
        description="Equipment Initial",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="ZD04",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    TransactionReferenceNumber: Optional[X12AN] = element(
        name="ZD05",
        description="Transaction Reference Number",
        min_length=1,
        max_length=50,
    )

    TransactionReferenceDate: Optional[X12DT] = element(
        name="ZD06",
        description="Transaction Reference Date",
        min_length=8,
        max_length=8,
    )

    CorrectionIndicator: X12ID = element(
        name="ZD07",
        description="Correction Indicator",
        mandatory=True,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="ZD08",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    EquipmentNumberCheckDigit: Optional[X12Nn] = element(
        name="ZD09",
        description="Equipment Number Check Digit",
        min_length=1,
        max_length=1,
    )
