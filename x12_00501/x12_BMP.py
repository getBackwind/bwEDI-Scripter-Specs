# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class BMP(Segment):
    """
    BMP - Beginning Segment for Market Development Fund Settlement
    
    Description:
        To indicate identifying numbers and other basic data relative to market development funds
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BMP/
    """
    _id: Literal["BMP"] = id_element(name="BMP")

    TransactionHandlingCode: X12ID = element(
        name="BMP01",
        description="Transaction Handling Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: X12AN = element(
        name="BMP02",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    PaymentMethodCode: Optional[X12ID] = element(
        name="BMP03",
        description="Payment Method Code",
        min_length=3,
        max_length=3,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="BMP04",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )
