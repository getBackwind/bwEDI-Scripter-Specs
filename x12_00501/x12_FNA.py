# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class FNA(Segment):
    """
    FNA - Financial Status Information
    
    Description:
        To provide financial status information about an applicant for a student loan
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FNA/
    """
    _id: Literal["FNA"] = id_element(name="FNA")

    YesNoConditionOrResponseCode: X12ID = element(
        name="FNA01",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: X12ID = element(
        name="FNA02",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: X12ID = element(
        name="FNA03",
        description="Yes/No Condition or Response Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    DependencyStatusCode: Optional[X12ID] = element(
        name="FNA04",
        description="Dependency Status Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode4: Optional[X12ID] = element(
        name="FNA05",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode5: Optional[X12ID] = element(
        name="FNA06",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
