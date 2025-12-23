# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class RQS(Segment):
    """
    RQS - Request for Information
    
    Description:
        To identify a question and a reply
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/RQS/
    """
    _id: Literal["RQS"] = id_element(name="RQS")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="RQS01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="RQS02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    Description: Optional[X12AN] = element(
        name="RQS03",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="RQS04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    Description2: Optional[X12AN] = element(
        name="RQS05",
        description="Description",
        min_length=1,
        max_length=80,
    )
