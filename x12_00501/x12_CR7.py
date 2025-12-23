# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class CR7(Segment):
    """
    CR7 - Home Health Treatment Plan Certification
    
    Description:
        To supply information related to the home health care plan of treatment and services
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CR7/
    """
    _id: Literal["CR7"] = id_element(name="CR7")

    DisciplineTypeCode: X12ID = element(
        name="CR701",
        description="Discipline Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Number: X12Nn = element(
        name="CR702",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    Number2: X12Nn = element(
        name="CR703",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )
