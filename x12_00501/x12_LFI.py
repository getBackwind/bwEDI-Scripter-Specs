# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12DT, X12ID, X12TM


class LFI(Segment):
    """
    LFI - Beginning Segment for Locomotive Information
    
    Description:
        To provide locomotive information between rail carriers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/LFI/
    """
    _id: Literal["LFI"] = id_element(name="LFI")

    StandardPointLocationCode: X12ID = element(
        name="LFI01",
        description="Standard Point Location Code",
        mandatory=True,
        min_length=6,
        max_length=9,
    )

    Date: X12DT = element(
        name="LFI02",
        description="Date",
        mandatory=True,
        min_length=8,
        max_length=8,
    )

    Time: X12TM = element(
        name="LFI03",
        description="Time",
        mandatory=True,
        min_length=4,
        max_length=8,
    )

    EquipmentStatusCode: X12ID = element(
        name="LFI04",
        description="Equipment Status Code",
        mandatory=True,
        min_length=1,
        max_length=2,
    )

    IndustryCode: X12AN = element(
        name="LFI05",
        description="Industry Code",
        mandatory=True,
        min_length=1,
        max_length=30,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="LFI06",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    IndustryCode3: Optional[X12AN] = element(
        name="LFI07",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    InterchangeTrainIdentification: Optional[X12AN] = element(
        name="LFI08",
        description="Interchange Train Identification",
        min_length=1,
        max_length=10,
    )
