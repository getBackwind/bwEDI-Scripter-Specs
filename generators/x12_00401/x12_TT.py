# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12Nn


class TT(Segment):
    """
    TT - Term Text
    
    Description:
        To specify general term text in a rate docket
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/TT/
    """
    _id: Literal["TT"] = id_element(name="TT")

    AssignedNumber: X12Nn = element(
        name="TT01",
        description="Assigned Number",
        mandatory=True,
        min_length=1,
        max_length=6,
    )

    FixedFormatInformation: X12AN = element(
        name="TT02",
        description="Fixed Format Information",
        mandatory=True,
        min_length=1,
        max_length=80,
    )
