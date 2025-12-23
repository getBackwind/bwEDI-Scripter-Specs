# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN


class Y5(Segment):
    """
    Y5 - Space Booking Cancellation
    
    Description:
        To specify booking number for cancellation
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/Y5/
    """
    _id: Literal["Y5"] = id_element(name="Y5")

    BookingNumber: X12AN = element(
        name="Y501",
        description="Booking Number",
        mandatory=True,
        min_length=1,
        max_length=17,
    )
