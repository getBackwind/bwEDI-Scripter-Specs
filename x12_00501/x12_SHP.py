# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R, X12TM


class SHP(Segment):
    """
    SHP - Shipped/Received Information
    
    Description:
        To specify shipment and/or receipt information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SHP/
    """
    _id: Literal["SHP"] = id_element(name="SHP")

    QuantityQualifier: Optional[X12ID] = element(
        name="SHP01",
        description="Quantity Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="SHP02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="SHP03",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    Date: Optional[X12DT] = element(
        name="SHP04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="SHP05",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="SHP06",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="SHP07",
        description="Time",
        min_length=4,
        max_length=8,
    )
