# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class UQS(Segment):
    """
    UQS - Underwriting Question
    
    Description:
        To report information provider underwriting data in a question and answer format
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/UQS/
    """
    _id: Literal["UQS"] = id_element(name="UQS")

    ReferenceIdentification: X12AN = element(
        name="UQS01",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: Optional[X12AN] = element(
        name="UQS02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    FreeFormMessageText: Optional[X12AN] = element(
        name="UQS03",
        description="Free-form Message Text",
        min_length=1,
        max_length=264,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="UQS04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
