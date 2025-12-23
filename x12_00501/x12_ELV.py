# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class ELV(Segment):
    """
    ELV - Employee Leave Summary
    
    Description:
        To provide summary information concerning the employeeï¿½s leave records
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/ELV/
    """
    _id: Literal["ELV"] = id_element(name="ELV")

    EmploymentStatusCode: X12ID = element(
        name="ELV01",
        description="Employment Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="ELV02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="ELV03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="ELV04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity3: Optional[X12R] = element(
        name="ELV05",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity4: Optional[X12R] = element(
        name="ELV06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
