# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class SA(Segment):
    """
    SA - Status Action
    
    Description:
        To identify a carrier and person taking action or making changes
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SA/
    """
    _id: Literal["SA"] = id_element(name="SA")

    Date: X12DT = element(
        name="SA01",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    ActionCode: X12ID = element(
        name="SA02",
        description="Action Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    StandardCarrierAlphaCode: X12ID = element(
        name="SA03",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Name: Optional[X12AN] = element(
        name="SA04",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Date2: Optional[X12DT] = element(
        name="SA05",
        description="Date",
        min_length=8,
        max_length=8,
    )
