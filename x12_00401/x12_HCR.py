# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class HCR(Segment):
    """
    HCR - Health Care Services Review
    
    Description:
        To specify the outcome of a health care services review
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/HCR/
    """
    _id: Literal["HCR"] = id_element(name="HCR")

    ActionCode: X12ID = element(
        name="HCR01",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="HCR02",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )

    RejectReasonCode: Optional[X12ID] = element(
        name="HCR03",
        description="Reject Reason Code",
        min_length=2,
        max_length=2,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="HCR04",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
