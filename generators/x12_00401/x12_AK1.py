# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn


class AK1(Segment):
    """
    AK1 - Functional Group Response Header
    
    Description:
        To start acknowledgment of a functional group
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/AK1/
    """
    _id: Literal["AK1"] = id_element(name="AK1")

    GroupCode: X12ID = element(
        name="AK101",
        description="Functional Identifier Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    GroupID: X12Nn = element(
        name="AK102",
        description="Group Control Number",
        mandatory=True,
        min_length=1,
        max_length=9,
    )
