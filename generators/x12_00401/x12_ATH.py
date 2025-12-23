# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID, X12R


class ATH(Segment):
    """
    ATH - Resource Authorization
    
    Description:
        To specify resource authorizations (i.e., finished labor, material, etc.) in the planning schedule
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/ATH/
    """
    _id: Literal["ATH"] = id_element(name="ATH")

    ResourceAuthorizationCode: X12ID = element(
        name="ATH01",
        description="Resource Authorization Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Date: Optional[X12DT] = element(
        name="ATH02",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Quantity: Optional[X12R] = element(
        name="ATH03",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Quantity2: Optional[X12R] = element(
        name="ATH04",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    Date2: Optional[X12DT] = element(
        name="ATH05",
        description="Date",
        min_length=8,
        max_length=8,
    )
