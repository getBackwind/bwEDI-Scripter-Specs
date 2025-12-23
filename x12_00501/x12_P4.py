# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12R, X12TM


class P4(Segment):
    """
    P4 - Port Information
    
    Description:
        To transmit identifying information for a port
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/P4/
    """
    _id: Literal["P4"] = id_element(name="P4")

    LocationIdentifier: X12AN = element(
        name="P401",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    Date: X12DT = element(
        name="P402",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Quantity: Optional[X12R] = element(
        name="P403",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    LocationIdentifier2: Optional[X12AN] = element(
        name="P404",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    Time: Optional[X12TM] = element(
        name="P405",
        description="Time",
        min_length=4,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="P406",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Time2: Optional[X12TM] = element(
        name="P407",
        description="Time",
        min_length=4,
        max_length=8,
    )
