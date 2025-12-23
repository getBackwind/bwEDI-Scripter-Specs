# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12R


class FRM(Segment):
    """
    FRM - Supporting Documentation
    
    Description:
        To specify information in response to a codified questionnaire document
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/FRM/
    """
    _id: Literal["FRM"] = id_element(name="FRM")

    AssignedIdentification: X12AN = element(
        name="FRM01",
        description="Assigned Identification",
        mandatory=True,
        min_length=1,
        max_length=20,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="FRM02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="FRM03",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date: Optional[X12DT] = element(
        name="FRM04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    PercentDecimalFormat: Optional[X12R] = element(
        name="FRM05",
        description="Percent, Decimal Format",
        min_length=1,
        max_length=6,
    )
