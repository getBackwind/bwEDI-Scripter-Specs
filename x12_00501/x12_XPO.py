# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class XPO(Segment):
    """
    XPO - Preassigned Purchase Order Numbers
    
    Description:
        To transmit preassigned purchase order numbers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/XPO/
    """
    _id: Literal["XPO"] = id_element(name="XPO")

    PurchaseOrderNumber: X12AN = element(
        name="XPO01",
        description="Purchase Order Number",
        mandatory=True,
        min_length=1,
        max_length=22,
    )

    PurchaseOrderNumber2: Optional[X12AN] = element(
        name="XPO02",
        description="Purchase Order Number",
        min_length=1,
        max_length=22,
    )

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="XPO03",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="XPO04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )
