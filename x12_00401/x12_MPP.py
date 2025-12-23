# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class MPP(Segment):
    """
    MPP - Mortgage Pool Program
    
    Description:
        To identify mortgage pool types
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/MPP/
    """
    _id: Literal["MPP"] = id_element(name="MPP")

    CodeCategory: X12ID = element(
        name="MPP01",
        description="Code Category",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    ProgramTypeCode: X12ID = element(
        name="MPP02",
        description="Program Type Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    DateTimeQualifier: Optional[X12ID] = element(
        name="MPP03",
        description="Date/Time Qualifier",
        min_length=3,
        max_length=3,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="MPP04",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="MPP05",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="MPP06",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    AccrualRateMethodCode: Optional[X12ID] = element(
        name="MPP07",
        description="Accrual Rate Method Code",
        min_length=1,
        max_length=1,
    )

    CertificationTypeCode: Optional[X12ID] = element(
        name="MPP08",
        description="Certification Type Code",
        min_length=1,
        max_length=1,
    )
