# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class CED(Segment):
    """
    CED - Administration of Justice Event Description
    
    Description:
        To describe specific administration of justice events and actions
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/CED/
    """
    _id: Literal["CED"] = id_element(name="CED")

    AdministrationOfJusticeEventTypeCode: X12ID = element(
        name="CED01",
        description="Administration of Justice Event Type Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    ActionCode: Optional[X12ID] = element(
        name="CED02",
        description="Action Code",
        min_length=1,
        max_length=2,
    )

    NoticeTypeCode: Optional[X12ID] = element(
        name="CED03",
        description="Notice Type Code",
        min_length=1,
        max_length=3,
    )

    CaseTypeCode: Optional[X12ID] = element(
        name="CED04",
        description="Case Type Code",
        min_length=1,
        max_length=2,
    )

    Description: Optional[X12AN] = element(
        name="CED05",
        description="Description",
        min_length=1,
        max_length=80,
    )
