# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12R


class EC(Segment):
    """
    EC - Employment Class
    
    Description:
        To provide class of employment information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/EC/
    """
    _id: Literal["EC"] = id_element(name="EC")

    EmploymentClassCode: Optional[X12ID] = element(
        name="EC01",
        description="Employment Class Code",
        min_length=2,
        max_length=2,
    )

    EmploymentClassCode2: Optional[X12ID] = element(
        name="EC02",
        description="Employment Class Code",
        min_length=2,
        max_length=2,
    )

    EmploymentClassCode3: Optional[X12ID] = element(
        name="EC03",
        description="Employment Class Code",
        min_length=2,
        max_length=2,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="EC04",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )

    InformationStatusCode: Optional[X12ID] = element(
        name="EC05",
        description="Information Status Code",
        min_length=1,
        max_length=1,
    )

    OccupationCode: Optional[X12ID] = element(
        name="EC06",
        description="Occupation Code",
        min_length=4,
        max_length=6,
    )
