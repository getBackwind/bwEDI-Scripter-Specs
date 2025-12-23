# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class DEL(Segment):
    """
    DEL - Delivery Logistics
    
    Description:
        To define delivery logistics
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/DEL/
    """
    _id: Literal["DEL"] = id_element(name="DEL")

    Quantity: X12R = element(
        name="DEL01",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    IdentificationCodeQualifier: X12ID = element(
        name="DEL02",
        description="Identification Code Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IdentificationCode: X12AN = element(
        name="DEL03",
        description="Identification Code",
        mandatory=True,
        min_length=2,
        max_length=80,
    )

    InvoiceNumber: Optional[X12AN] = element(
        name="DEL04",
        description="Invoice Number",
        min_length=1,
        max_length=22,
    )

    MoveTypeCode: Optional[X12ID] = element(
        name="DEL05",
        description="Move Type Code",
        min_length=1,
        max_length=1,
    )
