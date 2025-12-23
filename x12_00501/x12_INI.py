# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class INI(Segment):
    """
    INI - Incorporation Information
    
    Description:
        To provide basic information concerning a corporation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/INI/
    """
    _id: Literal["INI"] = id_element(name="INI")

    StateOrProvinceCode: X12ID = element(
        name="INI01",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: X12DT = element(
        name="INI02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    EntityTypeQualifier: Optional[X12ID] = element(
        name="INI03",
        description="Entity Type Qualifier",
        min_length=1,
        max_length=1,
    )
