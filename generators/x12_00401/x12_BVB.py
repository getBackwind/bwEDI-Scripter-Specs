# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class BVB(Segment):
    """
    BVB - Beginning Segment for Vehicle Baying Order
    
    Description:
        To indicate the beginning of the Vehicle Baying Order Transaction Set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BVB/
    """
    _id: Literal["BVB"] = id_element(name="BVB")

    StandardCarrierAlphaCode: X12ID = element(
        name="BVB01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="BVB02",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="BVB03",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    BayTypeCode: Optional[X12ID] = element(
        name="BVB04",
        description="Bay Type Code",
        min_length=1,
        max_length=1,
    )

    CapacityQualifier: Optional[X12ID] = element(
        name="BVB05",
        description="Capacity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="BVB06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    TransactionSetPurposeCode: Optional[X12ID] = element(
        name="BVB07",
        description="Transaction Set Purpose Code",
        min_length=2,
        max_length=2,
    )
