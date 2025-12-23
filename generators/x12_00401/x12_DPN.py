# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class DPN(Segment):
    """
    DPN - Dependent Information
    
    Description:
        To provide dependent information
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/DPN/
    """
    _id: Literal["DPN"] = id_element(name="DPN")

    Number: X12Nn = element(
        name="DPN01",
        description="Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )

    MaritalStatusCode: Optional[X12ID] = element(
        name="DPN02",
        description="Marital Status Code",
        min_length=1,
        max_length=1,
    )

    EmploymentStatusCode: Optional[X12ID] = element(
        name="DPN03",
        description="Employment Status Code",
        min_length=2,
        max_length=2,
    )

    Number2: Optional[X12Nn] = element(
        name="DPN04",
        description="Number",
        min_length=1,
        max_length=9,
    )
