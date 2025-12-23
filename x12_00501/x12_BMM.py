# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn, X12R


class BMM(Segment):
    """
    BMM - Beginning Segment for Multilevel Railcar Load Details Transaction
    
    Description:
        To indicate the beginning of the Multilevel Railcar Load Details Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BMM/
    """
    _id: Literal["BMM"] = id_element(name="BMM")

    StandardCarrierAlphaCode: X12ID = element(
        name="BMM01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    StandardPointLocationCode: X12ID = element(
        name="BMM02",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    Quantity: X12R = element(
        name="BMM03",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    WaybillNumber: X12Nn = element(
        name="BMM04",
        description="Waybill Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="BMM05",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    ShipmentIdentificationNumber: Optional[X12AN] = element(
        name="BMM06",
        description="Shipment Identification Number",
        min_length=1,
        max_length=30,
    )

    VehicleStatus: Optional[X12AN] = element(
        name="BMM07",
        description="Vehicle Status",
        min_length=1,
        max_length=2,
    )

    AccountNumber: Optional[X12AN] = element(
        name="BMM08",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BMM09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BMM10",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )
