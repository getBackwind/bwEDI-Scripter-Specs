# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12Nn


class ZC1(Segment):
    """
    ZC1 - Beginning Segment for Data Correction or Change
    
    Description:
        To transmit identifying numbers, dates, and other basic data relating to the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ZC1/
    """
    _id: Literal["ZC1"] = id_element(name="ZC1")

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="ZC101",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    EquipmentInitial: Optional[X12AN] = element(
        name="ZC102",
        description="Equipment Initial",
        min_length=1,
        max_length=4,
    )

    EquipmentNumber: X12AN = element(
        name="ZC103",
        description="Equipment Number",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    TransactionReferenceNumber: X12AN = element(
        name="ZC104",
        description="Transaction Reference Number",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    TransactionReferenceDate: X12DT = element(
        name="ZC105",
        description="Transaction Reference Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    CorrectionIndicator: X12ID = element(
        name="ZC106",
        description="Correction Indicator",
        mandatory=True,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="ZC107",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    TransportationMethodTypeCode: X12ID = element(
        name="ZC108",
        description="Transportation Method/Type Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    EquipmentNumberCheckDigit: Optional[X12Nn] = element(
        name="ZC109",
        description="Equipment Number Check Digit",
        min_length=1,
        max_length=1,
    )
