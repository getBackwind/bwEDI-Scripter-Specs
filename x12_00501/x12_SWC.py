# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class SWC(Segment):
    """
    SWC - Switching Conditions
    
    Description:
        To transmit data relating to the switching service being performed.
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/SWC/
    """
    _id: Literal["SWC"] = id_element(name="SWC")

    SwitchingSettlementCode: X12ID = element(
        name="SWC01",
        description="Switching Settlement Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    StandardPointLocationCode: X12ID = element(
        name="SWC02",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    AmountCharged: X12Nn = element(
        name="SWC03",
        description="Amount Charged",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    StandardPointLocationCode2: Optional[X12ID] = element(
        name="SWC04",
        description="Standard Point Location Code",
        min_length=6,
        max_length=9,
    )

    StandardCarrierAlphaCode: Optional[X12ID] = element(
        name="SWC05",
        description="Standard Carrier Alpha Code",
        min_length=2,
        max_length=4,
    )
