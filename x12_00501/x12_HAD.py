# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class HAD(Segment):
    """
    HAD - Hospital Affiliation Detail
    
    Description:
        To provide detail information describing a provider's affiliation to a specific hospital
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/HAD/
    """
    _id: Literal["HAD"] = id_element(name="HAD")

    StatusCode: X12ID = element(
        name="HAD01",
        description="Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="HAD02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="HAD03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="HAD04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode: Optional[X12ID] = element(
        name="HAD05",
        description="Code List Qualifier Code",
        min_length=1,
        max_length=3,
    )

    IndustryCode: Optional[X12AN] = element(
        name="HAD06",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )
