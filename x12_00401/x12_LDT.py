# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class LDT(Segment):
    """
    LDT - Lead Time
    
    Description:
        To specify lead time for availability of products and services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LDT/
    """
    _id: Literal["LDT"] = id_element(name="LDT")

    LeadTimeCode: X12ID = element(
        name="LDT01",
        description="Lead Time Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Quantity: X12R = element(
        name="LDT02",
        description="Quantity",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    UnitOfTimePeriodOrInterval: X12ID = element(
        name="LDT03",
        description="Unit of Time Period or Interval",
        mandatory=True,
    )

    Date: Optional[X12DT] = element(
        name="LDT04",
        description="Date",
        min_length=8,
        max_length=8,
    )
