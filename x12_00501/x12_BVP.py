# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BVP(Segment):
    """
    BVP - Beginning Segment for Vehicle Shipping Order
    
    Description:
        To indicate the beginning of the Vehicle Shipping Order Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BVP/
    """
    _id: Literal["BVP"] = id_element(name="BVP")

    VehicleProductionStatus: X12AN = element(
        name="BVP01",
        description="Vehicle Production Status",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="BVP02",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="BVP03",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    IdentificationCodeQualifier2: Optional[X12ID] = element(
        name="BVP04",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode2: Optional[X12AN] = element(
        name="BVP05",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    VehicleServiceCode: Optional[X12ID] = element(
        name="BVP06",
        description="Vehicle Service Code",
        min_length=2,
        max_length=2,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="BVP07",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    VehicleStatus: Optional[X12AN] = element(
        name="BVP08",
        description="Vehicle Status",
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BVP09",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date: Optional[X12DT] = element(
        name="BVP10",
        description="Date",
        min_length=8,
        max_length=8,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BVP11",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )
