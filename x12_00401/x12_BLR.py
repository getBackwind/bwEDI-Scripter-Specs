# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12DT, X12ID


class BLR(Segment):
    """
    BLR - Transportation Carrier Identification
    
    Description:
        To transmit the identifying SCAC code and effective date for the data in the transaction set
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/BLR/
    """
    _id: Literal["BLR"] = id_element(name="BLR")

    StandardCarrierAlphaCode: X12ID = element(
        name="BLR01",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    Date: Optional[X12DT] = element(
        name="BLR02",
        description="Date",
        min_length=8,
        max_length=8,
    )
