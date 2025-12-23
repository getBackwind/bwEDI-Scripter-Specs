# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class G4(Segment):
    """
    G4 - Scale Identification
    
    Description:
        To identify the scale type and the location and time a shipment is weighed
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/G4/
    """
    _id: Literal["G4"] = id_element(name="G4")

    CityName: X12AN = element(
        name="G401",
        description="City Name",
        mandatory=True,
        min_length=2,
        max_length=30,
    )

    StateOrProvinceCode: X12ID = element(
        name="G402",
        description="State or Province Code",
        mandatory=True,
        min_length=2,
        max_length=2,
    )

    Name: Optional[X12AN] = element(
        name="G403",
        description="Name",
        min_length=1,
        max_length=60,
    )

    Date: X12DT = element(
        name="G404",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: Optional[X12TM] = element(
        name="G405",
        description="Time",
        min_length=4,
        max_length=8,
    )

    ScaleTypeCode: Optional[X12ID] = element(
        name="G406",
        description="Scale Type Code",
        min_length=1,
        max_length=1,
    )
