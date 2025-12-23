# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class B9(Segment):
    """
    B9 - Beginning Segment for Logistics Services
    
    Description:
        To indicate the beginning of a logistics service transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/B9/
    """
    _id: Literal["B9"] = id_element(name="B9")

    ReferenceIdentification: X12AN = element(
        name="B901",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    TransactionSetPurposeCode: X12ID = element(
        name="B902",
        description="Transaction Set Purpose Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ShipmentMethodOfPayment: Optional[X12ID] = element(
        name="B903",
        description="Shipment Method of Payment",
    )
