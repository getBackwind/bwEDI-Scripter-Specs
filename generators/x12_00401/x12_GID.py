# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class GID(Segment):
    """
    GID - Group Identification
    
    Description:
        To identify each dose group name and dose group gender
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/GID/
    """
    _id: Literal["GID"] = id_element(name="GID")

    Name: X12AN = element(
        name="GID01",
        description="Name",
        mandatory=True,
        min_length=1,
        max_length=60,
    )

    GenderCode: X12ID = element(
        name="GID02",
        description="Gender Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    Name2: Optional[X12AN] = element(
        name="GID03",
        description="Name",
        min_length=1,
        max_length=60,
    )
