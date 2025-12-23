# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT


class X2(Segment):
    """
    X2 - Import License
    
    Description:
        To transmit import license number and effective dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/X2/
    """
    _id: Literal["X2"] = id_element(name="X2")

    ImportLicenseNumber: X12AN = element(
        name="X201",
        description="Import License Number",
        mandatory=True,
        min_length=6,
        max_length=30,
    )

    Date: Optional[X12DT] = element(
        name="X202",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date2: Optional[X12DT] = element(
        name="X203",
        description="Date",
        min_length=8,
        max_length=8,
    )

    ImportLicenseNumber2: Optional[X12AN] = element(
        name="X204",
        description="Import License Number",
        min_length=6,
        max_length=30,
    )

    Date3: Optional[X12DT] = element(
        name="X205",
        description="Date",
        min_length=8,
        max_length=8,
    )

    Date4: Optional[X12DT] = element(
        name="X206",
        description="Date",
        min_length=8,
        max_length=8,
    )
