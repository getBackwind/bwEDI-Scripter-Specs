# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class CSU(Segment):
    """
    CSU - Supplemental Course Data
    
    Description:
        To provide supplemental information on a course or a particular instance of a course
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/CSU/
    """
    _id: Literal["CSU"] = id_element(name="CSU")

    Name: Optional[X12AN] = element(
        name="CSU01",
        description="Name",
        min_length=1,
        max_length=60,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="CSU02",
        description="Reference Identification",
        min_length=1,
        max_length=50,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="CSU03",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="CSU04",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="CSU05",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="CSU06",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    InstructionalSettingCode: Optional[X12ID] = element(
        name="CSU07",
        description="Instructional Setting Code",
        min_length=1,
        max_length=2,
    )

    AcademicCreditTypeCode: Optional[X12ID] = element(
        name="CSU08",
        description="Academic Credit Type Code",
        min_length=1,
        max_length=1,
    )

    Quantity: Optional[X12R] = element(
        name="CSU09",
        description="Quantity",
        min_length=1,
        max_length=15,
    )
