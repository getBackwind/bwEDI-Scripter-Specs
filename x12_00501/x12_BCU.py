# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BCU(Segment):
    """
    BCU - Legal Claim Updates
    
    Description:
        To identify specific actions already taken on a legal claim, and/or indicate that information related to a previously filed claim is being updated by this transaction
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BCU/
    """
    _id: Literal["BCU"] = id_element(name="BCU")

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="BCU01",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="BCU02",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="BCU03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    YesNoConditionOrResponseCode4: Optional[X12ID] = element(
        name="BCU04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    ActionCode: Optional[X12ID] = element(
        name="BCU05",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="BCU06",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    Date: Optional[X12DT] = element(
        name="BCU07",
        description="Date",
        min_length=8,
        max_length=8,
    )
