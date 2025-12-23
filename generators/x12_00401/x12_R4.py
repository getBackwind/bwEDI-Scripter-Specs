# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class R4(Segment):
    """
    R4 - Port or Terminal
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/R4/
    """
    _id: Literal["R4"] = id_element(name="R4")

    PortOrTerminalFunctionCode: X12ID = element(
        name="R401",
        description="Port or Terminal Function Code",
        mandatory=True,
        min_length=1,
        max_length=1,
    )

    LocationQualifier: Optional[X12ID] = element(
        name="R402",
        description="Location Qualifier",
        min_length=1,
        max_length=2,
    )

    LocationIdentifier: Optional[X12AN] = element(
        name="R403",
        description="Location Identifier",
        min_length=1,
        max_length=30,
    )

    PortName: Optional[X12AN] = element(
        name="R404",
        description="Port Name",
        min_length=2,
        max_length=24,
    )

    CountryCode: Optional[X12ID] = element(
        name="R405",
        description="Country Code",
        min_length=2,
        max_length=3,
    )

    TerminalName: Optional[X12AN] = element(
        name="R406",
        description="Terminal Name",
        min_length=2,
        max_length=30,
    )

    PierNumber: Optional[X12AN] = element(
        name="R407",
        description="Pier Number",
        min_length=1,
        max_length=4,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="R408",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )
