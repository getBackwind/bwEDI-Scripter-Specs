# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class P5(Segment):
    """
    P5 - Port Information
    
    Description:
        To indicate port-related data
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/P5/
    """
    _id: Literal["P5"] = id_element(name="P5")

    PortOrTerminalFunctionCode: X12ID = element(
        name="P501",
        description="Port or Terminal Function Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    LocationQualifier: X12ID = element(
        name="P502",
        description="Location Qualifier",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: X12AN = element(
        name="P503",
        description="Location Identifier",
        mandatory=True,
        min_length=1,
        max_length=30,
    )
