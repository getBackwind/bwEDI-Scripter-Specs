# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class BVS(Segment):
    """
    BVS - Beginning Segment for Vehicle Service
    
    Description:
        To indicate the beginning of the Vehicle Service Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BVS/
    """
    _id: Literal["BVS"] = id_element(name="BVS")

    StandardCarrierAlphaCode: X12ID = element(
        name="BVS01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="BVS02",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="BVS03",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    Quantity: Optional[X12R] = element(
        name="BVS04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VehicleServiceCode: Optional[X12ID] = element(
        name="BVS05",
        description="Vehicle Service Code",
        min_length=2,
        max_length=2,
    )

    VehicleStatus: Optional[X12AN] = element(
        name="BVS06",
        description="Vehicle Status",
        min_length=1,
        max_length=2,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="BVS07",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="BVS08",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="BVS09",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    BillOfLadingWaybillNumber: Optional[X12AN] = element(
        name="BVS10",
        description="Bill of Lading/Waybill Number",
        min_length=1,
        max_length=12,
    )

    AccountNumber: Optional[X12AN] = element(
        name="BVS11",
        description="Account Number",
        min_length=1,
        max_length=35,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BVS12",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
