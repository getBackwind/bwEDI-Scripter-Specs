# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID


class BA2(Segment):
    """
    BA2 - Beginning Segment for Cargo Terminal Information
    
    Description:
        To indicate the beginning of the Cargo Terminal Information Transaction Set and transmit identifying numbers and dates
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/BA2/
    """
    _id: Literal["BA2"] = id_element(name="BA2")

    StandardCarrierAlphaCode: X12ID = element(
        name="BA201",
        description="Standard Carrier Alpha Code",
        mandatory=True,
        min_length=2,
        max_length=4,
    )

    VesselCode: X12ID = element(
        name="BA202",
        description="Vessel Code",
        mandatory=True,
        min_length=1,
        max_length=8,
    )

    FlightVoyageNumber: X12AN = element(
        name="BA203",
        description="Flight/Voyage Number",
        mandatory=True,
        min_length=2,
        max_length=10,
    )

    ReferenceIdentification: X12AN = element(
        name="BA204",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    ReferenceIdentification2: X12AN = element(
        name="BA205",
        description="Reference Identification",
        mandatory=True,
        min_length=1,
        max_length=50,
    )

    PierNumber: X12AN = element(
        name="BA206",
        description="Pier Number",
        mandatory=True,
        min_length=1,
        max_length=4,
    )

    PierName: X12AN = element(
        name="BA207",
        description="Pier Name",
        mandatory=True,
        min_length=2,
        max_length=14,
    )

    PortOrTerminalFunctionCode: Optional[X12ID] = element(
        name="BA208",
        description="Port or Terminal Function Code",
        min_length=1,
        max_length=1,
    )

    PortName: Optional[X12AN] = element(
        name="BA209",
        description="Port Name",
        min_length=2,
        max_length=24,
    )

    Date: Optional[X12DT] = element(
        name="BA210",
        description="Date",
        min_length=8,
        max_length=8,
    )

    VesselCodeQualifier: Optional[X12ID] = element(
        name="BA211",
        description="Vessel Code Qualifier",
        min_length=1,
        max_length=1,
    )
