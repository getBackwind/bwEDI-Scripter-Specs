# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class G42(Segment):
    """
    G42 - Promotion Announcement Identification
    
    Description:
        To identify promotion activities between trading partners
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G42/
    """
    _id: Literal["G42"] = id_element(name="G42")

    PromotionStatusCode: X12ID = element(
        name="G4201",
        description="Promotion Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    AllowanceOrChargeNumber: X12AN = element(
        name="G4202",
        description="Allowance or Charge Number",
        mandatory=True,
        min_length=1,
        max_length=16,
    )

    TransactionTypeCode: Optional[X12ID] = element(
        name="G4203",
        description="Transaction Type Code",
        min_length=2,
        max_length=2,
    )
