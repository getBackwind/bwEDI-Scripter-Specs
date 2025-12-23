# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class W5(Segment):
    """
    W5 - Carrier and Route Information
    
    Description:
        To specify carrier and routing sequences and details
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/W5/
    """
    _id: Literal["W5"] = id_element(name="W5")

    StandardCarrierAlphaCode: X12ID = element(
        name="W501",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    CityName: Optional[X12AN] = element(
        name="W502",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StandardCarrierAlphaCode2: Optional[X12ID] = element(
        name="W503",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    CityName2: Optional[X12AN] = element(
        name="W504",
        description="City Name",
        min_length=2,
        max_length=30,
    )

    StandardCarrierAlphaCode3: Optional[X12ID] = element(
        name="W505",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )

    CityName3: Optional[X12AN] = element(
        name="W506",
        description="City Name",
        min_length=2,
        max_length=30,
    )
