# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class HS(Segment):
    """
    HS - Health Screening
    
    Description:
        To provide the receiving school district with information about health screening activities
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/HS/
    """
    _id: Literal["HS"] = id_element(name="HS")

    IndustryCode: X12AN = element(
        name="HS01",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="HS02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="HS03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    StatusReasonCode: Optional[X12ID] = element(
        name="HS04",
        description="Status Reason Code",
        min_length=3,
        max_length=3,
    )

    CodeListQualifierCode: X12ID = element(
        name="HS05",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )
