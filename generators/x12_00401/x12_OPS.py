# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class OPS(Segment):
    """
    OPS - Program Subject Area and Eligibility
    
    Description:
        To provide the receiving educational institution or agency with information about the student's eligibility and participation in selected subject areas within other programs
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/OPS/
    """
    _id: Literal["OPS"] = id_element(name="OPS")

    IdentificationCodeQualifier: Optional[X12ID] = element(
        name="OPS01",
        description="Identification Code Qualifier",
        min_length=1,
        max_length=2,
    )

    IdentificationCode: Optional[X12AN] = element(
        name="OPS02",
        description="Identification Code",
        min_length=2,
        max_length=80,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="OPS03",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    InstructionalSettingCode: Optional[X12ID] = element(
        name="OPS04",
        description="Instructional Setting Code",
        min_length=1,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="OPS06",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
