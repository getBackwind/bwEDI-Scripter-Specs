# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12R, X12TM


class SR(Segment):
    """
    SR - Requested Service Schedule
    
    Description:
        To identify requested service schedules
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SR/
    """
    _id: Literal["SR"] = id_element(name="SR")

    AssignedIdentification: Optional[X12AN] = element(
        name="SR01",
        description="Assigned Identification",
        min_length=1,
        max_length=20,
    )

    DayRotation: Optional[X12AN] = element(
        name="SR02",
        description="Day Rotation",
        min_length=1,
        max_length=7,
    )

    Time: Optional[X12TM] = element(
        name="SR03",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="SR04",
        description="Time",
        min_length=4,
        max_length=8,
    )

    FreeFormMessage: Optional[X12AN] = element(
        name="SR05",
        description="Free-form Message",
        min_length=1,
        max_length=60,
    )

    UnitPrice: Optional[X12R] = element(
        name="SR06",
        description="Unit Price",
        min_length=1,
        max_length=17,
    )

    Quantity: Optional[X12R] = element(
        name="SR07",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Date: Optional[X12DT] = element(
        name="SR08",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="SR09",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ProductServiceID: Optional[X12AN] = element(
        name="SR10",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )

    ProductServiceID2: Optional[X12AN] = element(
        name="SR11",
        description="Product/Service ID",
        min_length=1,
        max_length=48,
    )
