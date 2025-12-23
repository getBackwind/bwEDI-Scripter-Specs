# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class EMT(Segment):
    """
    EMT - Employment
    
    Description:
        To specify employment information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EMT/
    """
    _id: Literal["EMT"] = id_element(name="EMT")

    CodeListQualifierCode: Optional[X12ID] = element(
        name="EMT01",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="EMT02",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="EMT03",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="EMT04",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    Description: Optional[X12AN] = element(
        name="EMT05",
        description="Description",
        min_length=1,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="EMT06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="EMT07",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="EMT08",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
