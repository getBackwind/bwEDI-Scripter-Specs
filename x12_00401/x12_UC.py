# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class UC(Segment):
    """
    UC - Underwriting Category
    
    Description:
        To identify the category of underwriting data being transmitted
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/UC/
    """
    _id: Literal["UC"] = id_element(name="UC")

    CodeCategory: X12ID = element(
        name="UC01",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="UC02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="UC03",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="UC04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
