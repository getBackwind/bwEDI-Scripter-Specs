# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class SCT(Segment):
    """
    SCT - School Type
    
    Description:
        To specify school type
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/SCT/
    """
    _id: Literal["SCT"] = id_element(name="SCT")

    AcademicCreditTypeCode: Optional[X12ID] = element(
        name="SCT01",
        description="Academic Credit Type Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="SCT02",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    SessionCode: Optional[X12ID] = element(
        name="SCT03",
        description="Session Code",
        min_length=1,
        max_length=1,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="SCT04",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="SCT05",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )
