# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID


class INQ(Segment):
    """
    INQ - Credit Inquiry Details
    
    Description:
        To identify results of credit inquiry
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/INQ/
    """
    _id: Literal["INQ"] = id_element(name="INQ")

    ResultsCode: X12ID = element(
        name="INQ01",
        description="Results Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    TypeOfAccountCode: Optional[X12ID] = element(
        name="INQ02",
        description="Type of Account Code",
        min_length=2,
        max_length=2,
    )
