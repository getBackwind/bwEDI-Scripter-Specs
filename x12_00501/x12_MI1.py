# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class MI1(Segment):
    """
    MI1 - Mileage Source
    
    Description:
        To identify the source of the mileage tables used to request or propose a rate and to indicate the tables version
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/MI1/
    """
    _id: Literal["MI1"] = id_element(name="MI1")

    MileageSourceCode: X12ID = element(
        name="MI101",
        description="Mileage Source Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: X12ID = element(
        name="MI102",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Number: Optional[X12Nn] = element(
        name="MI103",
        description="Number",
        min_length=1,
        max_length=9,
    )
