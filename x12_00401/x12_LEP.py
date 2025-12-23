# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID


class LEP(Segment):
    """
    LEP - EPA Required Data
    
    Description:
        To specify the Environmental Protection Agency (EPA) information relating to shipments of hazardous material
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/LEP/
    """
    _id: Literal["LEP"] = id_element(name="LEP")

    EPAWasteStreamNumberCode: Optional[X12ID] = element(
        name="LEP01",
        description="EPA Waste Stream Number Code",
        min_length=4,
        max_length=6,
    )

    WasteCharacteristicsCode: Optional[X12ID] = element(
        name="LEP02",
        description="Waste Characteristics Code",
        min_length=12,
        max_length=16,
    )

    StateOrProvinceCode: Optional[X12ID] = element(
        name="LEP03",
        description="State or Province Code",
        min_length=2,
        max_length=2,
    )

    ReferenceIdentification: Optional[X12AN] = element(
        name="LEP04",
        description="Reference Identification",
        min_length=1,
        max_length=30,
    )
