# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class IMM(Segment):
    """
    IMM - Immunization Status Code
    
    Description:
        To provide the receiving school district or postsecondary institution with a notice of the immunization status of the student
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/IMM/
    """
    _id: Literal["IMM"] = id_element(name="IMM")

    ImmunizationTypeCode: X12ID = element(
        name="IMM01",
        description="Immunization Type Code",
        mandatory=True,
        min_length=3,
        max_length=6,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="IMM02",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="IMM03",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    ImmunizationStatusCode: Optional[X12ID] = element(
        name="IMM04",
        description="Immunization Status Code",
        min_length=1,
        max_length=2,
    )

    ReportTypeCode: Optional[X12ID] = element(
        name="IMM05",
        description="Report Type Code",
        min_length=2,
        max_length=2,
    )
