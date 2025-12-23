# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class SCD(Segment):
    """
    SCD - Sales Commission Employee Detail
    
    Description:
        To provide additional detail for an employee participating in a sales commission program
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SCD/
    """
    _id: Literal["SCD"] = id_element(name="SCD")

    EmploymentStatusCode: X12ID = element(
        name="SCD01",
        description="Employment Status Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="SCD02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    EmploymentStatusCode2: Optional[X12ID] = element(
        name="SCD03",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    Date2: Optional[X12DT] = element(
        name="SCD04",
        description="Date",
        min_length=8,
        max_length=8,
    )

    AgencyQualifierCode: Optional[X12ID] = element(
        name="SCD05",
        description="Agency Qualifier Code",
        min_length=2,
        max_length=2,
    )

    IndustryCode: Optional[X12AN] = element(
        name="SCD06",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    GenderCode: Optional[X12ID] = element(
        name="SCD07",
        description="Gender Code",
        min_length=1,
        max_length=1,
    )
